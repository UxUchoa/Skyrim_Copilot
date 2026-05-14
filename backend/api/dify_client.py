from __future__ import annotations

import json
from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any

import httpx

from backend.api.schemas import ChatFile
from backend.api.settings import ApiSettings


class DifyConfigurationError(RuntimeError):
    """Raised when the backend cannot call Dify because config is incomplete."""


class DifyAPIError(RuntimeError):
    """Raised when Dify returns an invalid or failing response."""


@dataclass(frozen=True)
class DifyUploadedFile:
    upload_file_id: str
    name: str | None = None
    size: int | None = None
    mime_type: str | None = None


def build_chat_payload(
    *,
    query: str,
    user: str,
    files: list[ChatFile],
    conversation_id: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "inputs": {},
        "query": query,
        "response_mode": "streaming",
        "conversation_id": conversation_id or "",
        "user": user,
        "files": [file.to_dify_payload() for file in files],
    }
    return payload


def parse_dify_sse_line(line: str) -> dict[str, Any] | None:
    if not line.startswith("data:"):
        return None

    value = line.removeprefix("data:").strip()
    if not value or value == "[DONE]":
        return None

    try:
        payload = json.loads(value)
    except json.JSONDecodeError as exc:
        raise DifyAPIError("Dify returned an invalid SSE event.") from exc

    if not isinstance(payload, dict):
        raise DifyAPIError("Dify returned an unexpected SSE event payload.")
    return payload


class DifyClient:
    def __init__(self, settings: ApiSettings) -> None:
        if not settings.dify_api_key:
            raise DifyConfigurationError("DIFY_API_KEY is required to call Dify.")
        self.settings = settings
        self.headers = {"Authorization": f"Bearer {settings.dify_api_key}"}

    async def upload_file(
        self,
        *,
        filename: str,
        content: bytes,
        mime_type: str,
        user: str,
    ) -> DifyUploadedFile:
        async with httpx.AsyncClient(
            base_url=self.settings.dify_base_url,
            timeout=self.settings.dify_timeout_seconds,
        ) as client:
            response = await client.post(
                "/v1/files/upload",
                headers=self.headers,
                data={"user": user},
                files={"file": (filename, content, mime_type)},
            )

        if response.status_code >= 400:
            raise DifyAPIError(_format_dify_error(response))

        data = response.json()
        upload_file_id = data.get("id") or data.get("upload_file_id")
        if not upload_file_id:
            raise DifyAPIError("Dify upload response did not include a file id.")

        return DifyUploadedFile(
            upload_file_id=str(upload_file_id),
            name=data.get("name"),
            size=data.get("size"),
            mime_type=data.get("mime_type"),
        )

    async def stream_chat(
        self,
        *,
        query: str,
        user: str,
        files: list[ChatFile],
        conversation_id: str | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        payload = build_chat_payload(
            query=query,
            user=user,
            files=files,
            conversation_id=conversation_id,
        )

        async with httpx.AsyncClient(
            base_url=self.settings.dify_base_url,
            timeout=None,
        ) as client:
            async with client.stream(
                "POST",
                "/v1/chat-messages",
                headers={**self.headers, "Accept": "text/event-stream"},
                json=payload,
                timeout=self.settings.dify_timeout_seconds,
            ) as response:
                if response.status_code >= 400:
                    body = await response.aread()
                    raise DifyAPIError(
                        f"Dify API error {response.status_code}: "
                        f"{body.decode('utf-8', errors='replace')}"
                    )

                async for line in response.aiter_lines():
                    event = parse_dify_sse_line(line)
                    if event is not None:
                        yield event


def _format_dify_error(response: httpx.Response) -> str:
    body = response.text.strip()
    if not body:
        body = response.reason_phrase
    return f"Dify API error {response.status_code}: {body}"
