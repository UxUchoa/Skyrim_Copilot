from __future__ import annotations

import argparse
import re
from pathlib import Path


IMAGE_LINK_RE = re.compile(r"\[!\[[^\]]*]\([^)]*\)]\([^)]*\)")
IMAGE_RE = re.compile(r"!\[[^\]]*]\([^)]*\)")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*>", flags=re.IGNORECASE)
UESP_IMAGE_URL_RE = re.compile(r"(?:https?:)?//images\.uesp\.net/\S+")
EXCESS_BLANK_LINES_RE = re.compile(r"\n{3,}")


def sanitize_markdown(markdown: str) -> str:
    """Remove media references that make Dify try to download wiki images."""

    markdown = IMAGE_LINK_RE.sub("", markdown)
    markdown = IMAGE_RE.sub("", markdown)
    markdown = HTML_IMAGE_RE.sub("", markdown)
    markdown = UESP_IMAGE_URL_RE.sub("", markdown)
    markdown = EXCESS_BLANK_LINES_RE.sub("\n\n", markdown)
    return markdown.strip() + "\n"


def prepare_corpus(input_dir: Path, output_dir: Path, merged_filename: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    merged_path = output_dir / merged_filename

    markdown_files = sorted(
        path
        for path in input_dir.glob("*.md")
        if path.name != merged_filename and path.is_file()
    )

    if not markdown_files:
        raise SystemExit(f"Nenhum arquivo .md encontrado em {input_dir}")

    with merged_path.open("w", encoding="utf-8") as merged:
        for index, source_path in enumerate(markdown_files, start=1):
            sanitized = sanitize_markdown(source_path.read_text(encoding="utf-8"))
            target_path = output_dir / source_path.name
            target_path.write_text(sanitized, encoding="utf-8")

            if index > 1:
                merged.write("\n\n---\n\n")
            merged.write(sanitized)

    print(
        f"Corpus preparado: {len(markdown_files)} arquivos limpos em "
        f"{output_dir.as_posix()}"
    )
    print(f"Arquivo mesclado limpo: {merged_path.as_posix()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove imagens do corpus Markdown antes do upload no Dify."
    )
    parser.add_argument(
        "--input-dir",
        default="data/processed/dify_markdown",
        help="Diretorio com os Markdown originais.",
    )
    parser.add_argument(
        "--output-dir",
        default="data/processed/dify_markdown_text_only",
        help="Diretorio para os Markdown sem imagens.",
    )
    parser.add_argument(
        "--merged-filename",
        default="skyrim_dify_markdown_merged_text_only.md",
        help="Nome do arquivo mesclado limpo.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prepare_corpus(
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        merged_filename=args.merged_filename,
    )


if __name__ == "__main__":
    main()

