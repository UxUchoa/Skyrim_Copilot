from __future__ import annotations

from typing import Any

import httpx

from backend.ingest.mediawiki_client import MediaWikiClient


class FakePagedMediaWikiClient(MediaWikiClient):
    def __init__(self) -> None:
        super().__init__(delay_seconds=0)
        self.calls = 0

    def _get_json(
        self,
        client: httpx.Client,
        params: dict[str, Any],
    ) -> dict[str, Any]:
        self.calls += 1
        if self.calls == 1:
            return {
                "query": {
                    "categorymembers": [
                        {"title": "Skyrim:Bleak Falls Barrow"},
                    ]
                },
                "continue": {"cmcontinue": "page|2"},
            }
        return {
            "query": {
                "categorymembers": [
                    {"title": "Lore:Dragons"},
                ]
            }
        }


def test_category_members_follow_mediawiki_pagination() -> None:
    client = FakePagedMediaWikiClient()

    candidates = list(client.iter_category_members("Skyrim-Quests"))

    assert [candidate.title for candidate in candidates] == [
        "Skyrim:Bleak Falls Barrow",
        "Lore:Dragons",
    ]
    assert candidates[0].category == "Category:Skyrim-Quests"
    assert candidates[1].namespace == "Lore"
    assert client.calls == 2


def test_title_to_url_encodes_spaces_for_wiki_paths() -> None:
    client = MediaWikiClient()

    assert (
        client.title_to_url("Skyrim:Bleak Falls Barrow")
        == "https://en.uesp.net/wiki/Skyrim:Bleak_Falls_Barrow"
    )
    assert (
        client.title_to_url("Skyrim:Miscellaneous Quests/Raven Rock")
        == "https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests/Raven_Rock"
    )
