from __future__ import annotations

import json

from backend.ingest.mediawiki_client import WikiPageCandidate
from backend.pipeline.build_uesp_corpus import read_exported_urls, write_url_plan


def test_write_url_plan_and_read_exported_urls(tmp_path) -> None:
    url_plan_path = tmp_path / "url_plan.jsonl"
    manifest_path = tmp_path / "manifest.jsonl"

    write_url_plan(
        [
            WikiPageCandidate(
                title="Skyrim:Weapons",
                url="https://en.uesp.net/wiki/Skyrim:Weapons",
                source="hub",
                namespace="Skyrim",
            )
        ],
        url_plan_path,
    )
    manifest_path.write_text(
        json.dumps({"source_url": "https://en.uesp.net/wiki/Skyrim:Weapons"}) + "\n",
        encoding="utf-8",
    )

    plan_entry = json.loads(url_plan_path.read_text(encoding="utf-8"))

    assert plan_entry["source"] == "hub"
    assert plan_entry["namespace"] == "Skyrim"
    assert read_exported_urls(manifest_path) == {
        "https://en.uesp.net/wiki/Skyrim:Weapons"
    }
