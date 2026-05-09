from __future__ import annotations

from backend.ingest.uesp_scraper import CrawlConfig, UespCrawler


def test_crawler_allows_configured_skyrim_and_lore_prefixes() -> None:
    crawler = UespCrawler(
        CrawlConfig(allowed_path_prefixes=("/wiki/Skyrim:", "/wiki/Lore:"))
    )

    assert crawler.is_allowed_url("https://en.uesp.net/wiki/Skyrim:Daedric_Quests")
    assert crawler.is_allowed_url("https://en.uesp.net/wiki/Lore:Dragons")
    assert not crawler.is_allowed_url("https://en.uesp.net/wiki/Special:RecentChanges")
    assert not crawler.is_allowed_url("https://en.uesp.net/wiki/Oblivion:Oblivion")
