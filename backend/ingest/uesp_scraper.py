from __future__ import annotations

import hashlib
import time
from collections import deque
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable, Iterator
from urllib.parse import urljoin, urlparse, urlunparse

import httpx
from bs4 import BeautifulSoup


DEFAULT_USER_AGENT = (
    "SkyrimCopilotRAG/0.1 "
    "(educational RAG corpus builder; contact: local-development)"
)


@dataclass(frozen=True)
class ScrapedPage:
    url: str
    html: str
    retrieved_at: datetime
    depth: int


@dataclass(frozen=True)
class CrawlConfig:
    base_url: str = "https://en.uesp.net"
    allowed_path_prefixes: tuple[str, ...] = ("/wiki/Skyrim:",)
    max_pages: int = 100
    max_depth: int = 1
    delay_seconds: float = 1.0
    timeout_seconds: float = 20.0
    retries: int = 2
    raw_dir: Path | None = Path("data/raw/uesp")
    user_agent: str = DEFAULT_USER_AGENT


class UespCrawler:
    """Polite crawler for UESP Skyrim pages."""

    def __init__(self, config: CrawlConfig | None = None) -> None:
        self.config = config or CrawlConfig()
        self._base_netloc = urlparse(self.config.base_url).netloc.lower()

    def crawl(self, seeds: Iterable[str]) -> Iterator[ScrapedPage]:
        queue: deque[tuple[str, int]] = deque(
            (self.canonicalize(seed), 0) for seed in seeds
        )
        queued = {url for url, _ in queue}
        visited: set[str] = set()

        with httpx.Client(
            headers={"User-Agent": self.config.user_agent},
            timeout=self.config.timeout_seconds,
            follow_redirects=True,
        ) as client:
            while queue and len(visited) < self.config.max_pages:
                url, depth = queue.popleft()
                if url in visited or not self.is_allowed_url(url):
                    continue

                try:
                    html = self.fetch(client, url)
                except RuntimeError as exc:
                    print(f"Skipping {url}: {exc}")
                    visited.add(url)
                    continue

                retrieved_at = datetime.now(UTC)
                visited.add(url)

                if self.config.raw_dir is not None:
                    self.save_raw_html(url, html, retrieved_at)

                yield ScrapedPage(
                    url=url,
                    html=html,
                    retrieved_at=retrieved_at,
                    depth=depth,
                )

                if depth >= self.config.max_depth:
                    continue

                for link in self.extract_links(html, url):
                    if link not in visited and link not in queued:
                        queue.append((link, depth + 1))
                        queued.add(link)

    def fetch(self, client: httpx.Client, url: str) -> str:
        last_error: Exception | None = None

        for attempt in range(self.config.retries + 1):
            if attempt > 0 or self.config.delay_seconds > 0:
                time.sleep(self.config.delay_seconds)

            try:
                response = client.get(url)
                response.raise_for_status()
                return response.text
            except (httpx.HTTPStatusError, httpx.TransportError) as exc:
                last_error = exc
                if not self._should_retry(exc) or attempt >= self.config.retries:
                    break

        raise RuntimeError(f"Failed to fetch {url}") from last_error

    def extract_links(self, html: str, page_url: str) -> list[str]:
        soup = BeautifulSoup(html, "html.parser")
        links: list[str] = []

        for anchor in soup.find_all("a", href=True):
            href = anchor.get("href", "")
            if self._is_noise_href(href):
                continue

            absolute_url = urljoin(page_url, href)
            canonical_url = self.canonicalize(absolute_url)
            if self.is_allowed_url(canonical_url):
                links.append(canonical_url)

        return sorted(set(links))

    def is_allowed_url(self, url: str) -> bool:
        parsed = urlparse(url)
        return (
            parsed.scheme in {"http", "https"}
            and parsed.netloc.lower() == self._base_netloc
            and parsed.path.startswith(self.config.allowed_path_prefixes)
        )

    def canonicalize(self, url: str) -> str:
        absolute = urljoin(self.config.base_url, url)
        parsed = urlparse(absolute)
        clean = parsed._replace(fragment="", query="")
        return urlunparse(clean)

    def save_raw_html(self, url: str, html: str, retrieved_at: datetime) -> Path:
        if self.config.raw_dir is None:
            raise ValueError("raw_dir must be configured before saving raw HTML.")

        self.config.raw_dir.mkdir(parents=True, exist_ok=True)
        filename = self._raw_filename(url)
        path = self.config.raw_dir / filename
        metadata = (
            f"<!-- source_url: {url} -->\n"
            f"<!-- retrieved_at: {retrieved_at.isoformat()} -->\n"
        )
        path.write_text(metadata + html, encoding="utf-8")
        return path

    def _raw_filename(self, url: str) -> str:
        parsed = urlparse(url)
        slug = parsed.path.removeprefix("/wiki/").replace("/", "_").replace(":", "_")
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
        safe_slug = "".join(char if char.isalnum() or char in "-_" else "_" for char in slug)
        return f"{safe_slug[:90]}_{digest}.html"

    def _is_noise_href(self, href: str) -> bool:
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            return True

        parsed = urlparse(href)
        if parsed.query:
            return True

        path = parsed.path or href
        noisy_fragments = (
            "/w/index.php",
            "/wiki/Special:",
            "/wiki/File:",
            "/wiki/Help:",
            "/wiki/Template:",
            "/wiki/Category:",
            "/wiki/User:",
            "/wiki/User_talk:",
            "/wiki/Talk:",
        )
        return any(fragment in path for fragment in noisy_fragments)

    def _should_retry(self, exc: Exception) -> bool:
        if isinstance(exc, httpx.TransportError):
            return True
        if isinstance(exc, httpx.HTTPStatusError):
            status_code = exc.response.status_code
            return status_code == 429 or 500 <= status_code < 600
        return False
