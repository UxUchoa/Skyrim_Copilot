from __future__ import annotations

import hashlib
from dataclasses import dataclass

from backend.rag.documents import RagDocument, RagSection


@dataclass(frozen=True)
class RagChunk:
    chunk_id: str
    title: str
    source_url: str
    entity_type: str
    namespace: str
    section_path: str
    markdown: str
    tags: list[str]


class SectionChunker:
    """Chunks documents by semantic sections, splitting only when needed."""

    def __init__(self, max_chars: int = 3_000) -> None:
        if max_chars < 500:
            raise ValueError("max_chars must be at least 500 for useful RAG context.")
        self.max_chars = max_chars

    def chunk(self, document: RagDocument) -> list[RagChunk]:
        chunks: list[RagChunk] = []
        for section in document.sections:
            section_chunks = self._split_section(section)
            for index, markdown in enumerate(section_chunks, start=1):
                section_path = section.heading
                if len(section_chunks) > 1:
                    section_path = f"{section.heading} / Part {index}"

                chunk_id = self._chunk_id(document.source_url, section_path)
                chunks.append(
                    RagChunk(
                        chunk_id=chunk_id,
                        title=document.title,
                        source_url=document.source_url,
                        entity_type=document.entity_type,
                        namespace=document.namespace,
                        section_path=section_path,
                        markdown=markdown,
                        tags=document.tags,
                    )
                )
        return chunks

    def _split_section(self, section: RagSection) -> list[str]:
        heading_prefix = f"{'#' * min(max(section.level, 2), 4)} {section.heading}"
        full_text = f"{heading_prefix}\n\n{section.markdown}".strip()
        if len(full_text) <= self.max_chars:
            return [full_text]

        chunks: list[str] = []
        current_parts: list[str] = [heading_prefix]
        current_size = len(heading_prefix)

        for paragraph in section.markdown.split("\n\n"):
            paragraph = paragraph.strip()
            if not paragraph:
                continue

            projected_size = current_size + len(paragraph) + 2
            if projected_size > self.max_chars and len(current_parts) > 1:
                chunks.append("\n\n".join(current_parts).strip())
                current_parts = [heading_prefix, paragraph]
                current_size = len(heading_prefix) + len(paragraph) + 2
            else:
                current_parts.append(paragraph)
                current_size = projected_size

        if len(current_parts) > 1:
            chunks.append("\n\n".join(current_parts).strip())

        return chunks

    def _chunk_id(self, source_url: str, section_path: str) -> str:
        digest = hashlib.sha1(f"{source_url}#{section_path}".encode("utf-8")).hexdigest()
        return digest[:16]
