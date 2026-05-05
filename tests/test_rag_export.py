from __future__ import annotations

import json
from datetime import UTC, datetime

from backend.rag.chunker import SectionChunker
from backend.rag.documents import RagDocument, RagSection
from backend.rag.markdown_exporter import MarkdownCorpusExporter


def test_chunker_preserves_section_heading_context() -> None:
    document = RagDocument(
        title="Whiterun",
        source_url="https://en.uesp.net/wiki/Skyrim:Whiterun",
        entity_type="location",
        retrieved_at=datetime(2024, 1, 1, tzinfo=UTC),
        sections=[
            RagSection(
                heading="Overview",
                level=2,
                markdown="Whiterun is a major city.\n\n" * 30,
            )
        ],
        tags=["Skyrim-Places"],
    )

    chunks = SectionChunker(max_chars=550).chunk(document)

    assert len(chunks) > 1
    assert all(chunk.markdown.startswith("## Overview") for chunk in chunks)
    assert all(chunk.entity_type == "location" for chunk in chunks)
    assert all(chunk.namespace == "unknown" for chunk in chunks)


def test_exporter_writes_markdown_and_manifest(tmp_path) -> None:
    document = RagDocument(
        title="Dragonstone",
        source_url="https://en.uesp.net/wiki/Skyrim:Dragonstone",
        entity_type="item",
        retrieved_at=datetime(2024, 1, 1, tzinfo=UTC),
        sections=[RagSection(heading="Overview", level=2, markdown="A quest item.")],
        tags=["Skyrim-Items"],
    )
    chunks = SectionChunker().chunk(document)
    exporter = MarkdownCorpusExporter()
    manifest_path = tmp_path / "manifest.jsonl"

    exporter.reset_manifest(manifest_path)
    markdown_path = exporter.export_document(
        document,
        output_dir=tmp_path / "dify_markdown",
        manifest_path=manifest_path,
        chunks=chunks,
    )

    markdown = markdown_path.read_text(encoding="utf-8")
    manifest_entry = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert 'source_url: "https://en.uesp.net/wiki/Skyrim:Dragonstone"' in markdown
    assert 'namespace: "unknown"' in markdown
    assert "# Dragonstone" in markdown
    assert manifest_entry["title"] == "Dragonstone"
    assert manifest_entry["namespace"] == "unknown"
    assert manifest_entry["chunks"][0]["section_path"] == "Overview"
