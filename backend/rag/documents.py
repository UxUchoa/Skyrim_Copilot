from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class RagSection:
    heading: str
    level: int
    markdown: str


@dataclass(frozen=True)
class RagDocument:
    title: str
    source_url: str
    entity_type: str
    retrieved_at: datetime
    sections: list[RagSection]
    namespace: str = "unknown"
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)

    @property
    def slug(self) -> str:
        value = self.title.strip().lower().replace(" ", "-")
        return "".join(char if char.isalnum() or char in "-_" else "-" for char in value)
