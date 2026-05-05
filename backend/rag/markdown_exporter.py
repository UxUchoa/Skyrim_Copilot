from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

from backend.rag.chunker import RagChunk
from backend.rag.documents import RagDocument


class MarkdownCorpusExporter:
    """Writes Dify-friendly Markdown files and a JSONL audit manifest."""

    def export_document(
        self,
        document: RagDocument,
        output_dir: Path,
        manifest_path: Path,
        chunks: Iterable[RagChunk],
    ) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)

        markdown_path = output_dir / self._filename(document)
        markdown_path.write_text(self.render_document(document), encoding="utf-8")

        chunk_list = list(chunks)
        with manifest_path.open("a", encoding="utf-8") as manifest:
            manifest.write(
                json.dumps(
                    {
                        "title": document.title,
                        "source_url": document.source_url,
                        "entity_type": document.entity_type,
                        "namespace": document.namespace,
                        "retrieved_at": document.retrieved_at.isoformat(),
                        "markdown_path": str(markdown_path.as_posix()),
                        "tags": document.tags,
                        "links": document.links,
                        "chunks": [
                            {
                                "chunk_id": chunk.chunk_id,
                                "section_path": chunk.section_path,
                                "chars": len(chunk.markdown),
                            }
                            for chunk in chunk_list
                        ],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

        return markdown_path

    def render_document(self, document: RagDocument) -> str:
        frontmatter = {
            "source_url": document.source_url,
            "title": document.title,
            "entity_type": document.entity_type,
            "namespace": document.namespace,
            "retrieved_at": document.retrieved_at.isoformat(),
            "tags": document.tags,
        }

        lines = ["---"]
        for key, value in frontmatter.items():
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        lines.extend(["---", "", f"# {document.title}", ""])

        for section in document.sections:
            heading_level = min(max(section.level, 2), 4)
            lines.append(f"{'#' * heading_level} {section.heading}")
            lines.append("")
            lines.append(section.markdown)
            lines.append("")

        return "\n".join(lines).strip() + "\n"

    def reset_manifest(self, manifest_path: Path) -> None:
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text("", encoding="utf-8")

    def _filename(self, document: RagDocument) -> str:
        digest = hashlib.sha1(document.source_url.encode("utf-8")).hexdigest()[:8]
        return f"{document.slug[:90]}_{digest}.md"
