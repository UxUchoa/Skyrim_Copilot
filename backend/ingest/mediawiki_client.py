from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Iterator
from urllib.parse import quote

import httpx

from backend.ingest.uesp_scraper import DEFAULT_USER_AGENT


@dataclass(frozen=True)
class WikiPageCandidate:
    title: str
    url: str
    source: str
    namespace: str
    category: str | None = None


class MediaWikiClient:
    """Small MediaWiki API client for UESP discovery."""

    def __init__(
        self,
        base_url: str = "https://en.uesp.net",
        *,
        delay_seconds: float = 0.25,
        timeout_seconds: float = 20.0,
        user_agent: str = DEFAULT_USER_AGENT,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_url = f"{self.base_url}/w/api.php"
        self.delay_seconds = delay_seconds
        self.timeout_seconds = timeout_seconds
        self.user_agent = user_agent

    def iter_category_members(
        self,
        category: str,
        *,
        max_pages: int | None = None,
    ) -> Iterator[WikiPageCandidate]:
        normalized_category = self._normalize_category(category)
        emitted = 0
        params: dict[str, Any] = {
            "action": "query",
            "format": "json",
            "list": "categorymembers",
            "cmtitle": normalized_category,
            "cmtype": "page",
            "cmlimit": "max",
        }

        with httpx.Client(
            headers={"User-Agent": self.user_agent},
            timeout=self.timeout_seconds,
            follow_redirects=True,
        ) as client:
            while True:
                if self.delay_seconds > 0:
                    time.sleep(self.delay_seconds)

                payload = self._get_json(client, params)
                members = payload.get("query", {}).get("categorymembers", [])
                for member in members:
                    title = str(member.get("title", "")).strip()
                    if not title:
                        continue
                    yield WikiPageCandidate(
                        title=title,
                        url=self.title_to_url(title),
                        source="category",
                        namespace=self.infer_namespace(title),
                        category=normalized_category,
                    )
                    emitted += 1
                    if max_pages is not None and emitted >= max_pages:
                        return

                continuation = payload.get("continue", {}).get("cmcontinue")
                if not continuation:
                    return
                params["cmcontinue"] = continuation

    def title_to_url(self, title: str) -> str:
        encoded_title = quote(title.replace(" ", "_"), safe=":/_()'!,")
        return f"{self.base_url}/wiki/{encoded_title}"

    def infer_namespace(self, title: str) -> str:
        if ":" not in title:
            return "Main"
        return title.split(":", maxsplit=1)[0]

    def _get_json(self, client: httpx.Client, params: dict[str, Any]) -> dict[str, Any]:
        response = client.get(self.api_url, params=params)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            code = data["error"].get("code", "unknown")
            info = data["error"].get("info", "MediaWiki API error")
            raise RuntimeError(f"MediaWiki API error {code}: {info}")
        return data

    def _normalize_category(self, category: str) -> str:
        category = category.strip()
        if category.startswith("Category:"):
            return category
        return f"Category:{category}"
