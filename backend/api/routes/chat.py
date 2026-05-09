from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse

from backend.api.dify_client import DifyAPIError, DifyClient, DifyConfigurationError
from backend.api.schemas import ChatStreamRequest
from backend.api.settings import ApiSettings, get_settings

router = APIRouter(tags=["chat"])


def encode_sse(event: str, data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return f"event: {event}\ndata: {payload}\n\n"


@router.post("/chat/stream")
async def chat_stream(
    request: ChatStreamRequest,
    settings: ApiSettings = Depends(get_settings),
) -> StreamingResponse:
    try:
        client = DifyClient(settings)
    except DifyConfigurationError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    user = request.user or settings.dify_default_user

    async def events() -> AsyncIterator[str]:
        last_conversation_id = request.conversation_id
        try:
            async for dify_event in client.stream_chat(
                query=request.query,
                user=user,
                files=request.files,
                conversation_id=request.conversation_id,
            ):
                conversation_id = dify_event.get("conversation_id")
                if conversation_id and conversation_id != last_conversation_id:
                    last_conversation_id = str(conversation_id)
                    yield encode_sse(
                        "conversation_id",
                        {"conversation_id": last_conversation_id},
                    )

                event_name = str(dify_event.get("event", "message"))
                # Dify emits `message` for Chatbot apps and `agent_message` for Agent apps;
                # both carry incremental answer chunks, so we normalize them downstream.
                if event_name in {"agent_message", "message"}:
                    yield encode_sse(
                        "agent_message",
                        {
                            "answer": dify_event.get("answer", ""),
                            "conversation_id": conversation_id,
                            "message_id": dify_event.get("message_id"),
                        },
                    )
                elif event_name == "error":
                    yield encode_sse(
                        "error",
                        {
                            "message": dify_event.get("message", "Dify stream error."),
                            "code": dify_event.get("code"),
                        },
                    )
                elif event_name == "message_end":
                    yield encode_sse(
                        "message_end",
                        {
                            "conversation_id": conversation_id,
                            "message_id": dify_event.get("message_id"),
                            "metadata": dify_event.get("metadata"),
                        },
                    )
        except DifyAPIError as exc:
            yield encode_sse("error", {"message": str(exc)})

    return StreamingResponse(
        events(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
