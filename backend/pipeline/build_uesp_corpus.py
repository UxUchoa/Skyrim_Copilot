from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from backend.ingest.mediawiki_client import MediaWikiClient, WikiPageCandidate
from backend.ingest.uesp_parser import UespParser
from backend.ingest.uesp_scraper import CrawlConfig, UespCrawler
from backend.ingest.uesp_seed_catalog import get_scope, iter_hub_candidates
from backend.rag.chunker import SectionChunker
from backend.rag.markdown_exporter import MarkdownCorpusExporter


DEFAULT_SEED = "https://en.uesp.net/wiki/Skyrim:Skyrim"


def main() -> None:
    args = parse_args()
    scope = get_scope(args.scope)
    client = MediaWikiClient(
        base_url=args.base_url,
        delay_seconds=args.api_delay_seconds,
    )
    candidates = discover_candidates(args, client)
    if args.resume:
        exported_urls = read_exported_urls(Path(args.manifest_path))
        candidates = [
            candidate for candidate in candidates if candidate.url not in exported_urls
        ]
    seeds = [candidate.url for candidate in candidates]
    write_url_plan(candidates, Path(args.url_plan_path))

    raw_dir = None if args.no_raw else Path(args.raw_dir)
    crawler = UespCrawler(
        CrawlConfig(
            base_url=args.base_url,
            allowed_path_prefixes=scope.allowed_prefixes,
            max_pages=args.max_pages,
            max_depth=args.max_depth,
            delay_seconds=args.delay_seconds,
            raw_dir=raw_dir,
        )
    )
    parser = UespParser()
    chunker = SectionChunker(max_chars=args.chunk_chars)
    exporter = MarkdownCorpusExporter()

    output_dir = Path(args.output_dir)
    manifest_path = Path(args.manifest_path)
    if not args.resume:
        exporter.reset_manifest(manifest_path)

    exported_count = 0
    for scraped_page in crawler.crawl(seeds):
        try:
            document = parser.parse(
                scraped_page.html,
                source_url=scraped_page.url,
                retrieved_at=scraped_page.retrieved_at,
            )
            chunks = chunker.chunk(document)
            markdown_path = exporter.export_document(
                document,
                output_dir=output_dir,
                manifest_path=manifest_path,
                chunks=chunks,
            )
        except Exception as exc:
            print(f"Skipping {scraped_page.url}: failed to parse/export page: {exc}")
            continue

        exported_count += 1
        print(
            f"Exported {document.title} "
            f"({len(chunks)} chunks) -> {markdown_path.as_posix()}"
        )

    print(f"Done. Exported {exported_count} pages. Manifest: {manifest_path.as_posix()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Dify-ready Markdown corpus from UESP Skyrim pages."
    )
    parser.add_argument(
        "--discovery",
        choices=("api", "crawl", "hybrid"),
        default="hybrid",
        help="URL discovery strategy before fetching page HTML.",
    )
    parser.add_argument(
        "--scope",
        choices=("skyrim", "all"),
        default="all",
        help="Content scope. 'all' allows Skyrim gameplay and Lore pages.",
    )
    parser.add_argument(
        "--seed",
        action="append",
        dest="seeds",
        help="Seed URL to crawl. Can be passed multiple times.",
    )
    parser.add_argument(
        "--seeds-file",
        help="Optional file containing one seed URL per line.",
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("UESP_BASE_URL", "https://en.uesp.net"),
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=int(os.getenv("UESP_DEFAULT_MAX_PAGES", "100")),
    )
    parser.add_argument("--max-depth", type=int, default=1)
    parser.add_argument(
        "--delay-seconds",
        type=float,
        default=float(os.getenv("UESP_DEFAULT_DELAY_SECONDS", "1.0")),
    )
    parser.add_argument(
        "--api-delay-seconds",
        type=float,
        default=float(os.getenv("UESP_API_DELAY_SECONDS", "0.25")),
    )
    parser.add_argument(
        "--raw-dir",
        default=os.getenv("UESP_RAW_DIR", "data/raw/uesp"),
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("UESP_PROCESSED_DIR", "data/processed/dify_markdown"),
    )
    parser.add_argument(
        "--manifest-path",
        default=os.getenv("UESP_MANIFEST_PATH", "data/processed/manifest.jsonl"),
    )
    parser.add_argument(
        "--url-plan-path",
        default=os.getenv("UESP_URL_PLAN_PATH", "data/processed/url_plan.jsonl"),
    )
    parser.add_argument("--chunk-chars", type=int, default=3_000)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Append to the existing manifest and skip already exported source URLs.",
    )
    parser.add_argument(
        "--no-raw",
        action="store_true",
        help="Do not persist raw HTML snapshots.",
    )
    return parser.parse_args()


def collect_seeds(args: argparse.Namespace) -> list[str]:
    seeds = list(args.seeds or [])
    if args.seeds_file:
        seed_file = Path(args.seeds_file)
        seeds.extend(
            line.strip()
            for line in seed_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    return seeds or [DEFAULT_SEED]


def discover_candidates(
    args: argparse.Namespace,
    client: MediaWikiClient,
) -> list[WikiPageCandidate]:
    scope = get_scope(args.scope)
    candidates: list[WikiPageCandidate] = []
    seen_urls: set[str] = set()

    def add(candidate: WikiPageCandidate) -> None:
        if candidate.url in seen_urls:
            return
        candidates.append(candidate)
        seen_urls.add(candidate.url)

    if args.discovery in {"crawl", "hybrid"}:
        for seed in collect_seeds(args):
            title = seed.rstrip("/").rsplit("/", maxsplit=1)[-1].replace("_", " ")
            add(
                WikiPageCandidate(
                    title=title,
                    url=client.title_to_url(title) if ":" in title else seed,
                    source="seed",
                    namespace=client.infer_namespace(title),
                )
            )

    if args.discovery in {"api", "hybrid"}:
        if args.discovery == "hybrid":
            for candidate in iter_hub_candidates(scope, client):
                add(candidate)

        for category in scope.categories:
            remaining = args.max_pages - len(candidates)
            if remaining <= 0:
                break
            for candidate in client.iter_category_members(category, max_pages=remaining):
                add(candidate)
                if len(candidates) >= args.max_pages:
                    break

    return candidates[: args.max_pages]


def write_url_plan(candidates: list[WikiPageCandidate], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as plan:
        for index, candidate in enumerate(candidates, start=1):
            plan.write(
                json.dumps(
                    {
                        "order": index,
                        "title": candidate.title,
                        "url": candidate.url,
                        "source": candidate.source,
                        "namespace": candidate.namespace,
                        "category": candidate.category,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )


def read_exported_urls(manifest_path: Path) -> set[str]:
    if not manifest_path.exists():
        return set()

    urls: set[str] = set()
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        source_url = entry.get("source_url")
        if isinstance(source_url, str):
            urls.add(source_url)
    return urls


if __name__ == "__main__":
    main()
