from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def bundle(
    input_dir: Path,
    output_dir: Path,
    pages_per_bundle: int,
) -> None:
    source_files = sorted(
        f
        for f in input_dir.glob("*.md")
        if "merged" not in f.name and "bundle" not in f.name
    )

    if not source_files:
        raise SystemExit(f"Nenhum .md encontrado em {input_dir}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    total_bundles = (len(source_files) + pages_per_bundle - 1) // pages_per_bundle
    pad = len(str(total_bundles))

    for bundle_index, chunk_start in enumerate(
        range(0, len(source_files), pages_per_bundle), start=1
    ):
        chunk = source_files[chunk_start : chunk_start + pages_per_bundle]
        bundle_name = f"skyrim_bundle_{str(bundle_index).zfill(pad)}_of_{total_bundles}.md"
        bundle_path = output_dir / bundle_name

        with bundle_path.open("w", encoding="utf-8") as out:
            for page_index, source_path in enumerate(chunk):
                if page_index > 0:
                    out.write("\n\n---\n\n")
                out.write(source_path.read_text(encoding="utf-8").rstrip())
                out.write("\n")

        size_kb = bundle_path.stat().st_size / 1024
        print(
            f"  bundle {bundle_index:>{pad}}/{total_bundles}  "
            f"{len(chunk):>3} paginas  {size_kb:>7.1f} KB  ->  {bundle_path.name}"
        )

    print(
        f"\nPronto: {total_bundles} bundles em '{output_dir}' "
        f"(~{pages_per_bundle} páginas cada)"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Divide o corpus Skyrim em bundles menores para upload no Dify."
    )
    parser.add_argument(
        "--input-dir",
        default="data/processed/dify_markdown_text_only",
        help="Diretório com os .md individuais sem imagens.",
    )
    parser.add_argument(
        "--output-dir",
        default="data/processed/dify_bundles",
        help="Diretório de saída dos bundles.",
    )
    parser.add_argument(
        "--pages-per-bundle",
        type=int,
        default=50,
        help="Páginas wiki por bundle (padrão: 50).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bundle(
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        pages_per_bundle=args.pages_per_bundle,
    )


if __name__ == "__main__":
    main()
