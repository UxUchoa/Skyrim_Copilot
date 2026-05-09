from __future__ import annotations

import re
from datetime import datetime
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as html_to_markdown

from backend.rag.documents import RagDocument, RagSection


NOISE_SELECTORS = [
    "script",
    "style",
    "noscript",
    "form",
    "#toc",
    ".toc",
    ".mw-editsection",
    ".printfooter",
    ".catlinks",
    ".noprint",
    ".metadata",
    ".ambox",
    ".navbox",
    ".vertical-navbox",
    ".notice",
    ".magnify",
]

LOW_VALUE_SECTION_HEADINGS = {
    "see also",
    "references",
    "external links",
}

ENTITY_RULES = (
    (("quest", "quests", "main quest", "side quest", "daedric quest"), "quest"),
    (("weapon", "weapons", "arrows", "bows"), "weapon"),
    (("armor", "armour", "clothing", "shields"), "armor"),
    (("place", "places", "location", "locations", "cities", "holds", "dungeons"), "location"),
    (("people", "npcs", "npc", "characters"), "npc"),
    (("book", "books", "journals", "notes"), "book"),
    (("spell", "spells", "magic effects", "shouts"), "spell"),
    (("creature", "creatures", "animals", "monsters"), "creature"),
    (("faction", "factions", "organizations"), "faction"),
    (("skill", "skills", "perks"), "skill"),
    (("ingredient", "ingredients", "alchemy"), "ingredient"),
    (("artifact", "artifacts", "unique items"), "artifact"),
    (("race", "races"), "race"),
    (("deity", "deities", "gods", "aedra", "daedra"), "deity"),
    (("history", "events", "mythology"), "lore"),
    (("item", "items"), "item"),
)


class UespParser:
    """Converts UESP MediaWiki HTML into normalized RAG documents."""

    def parse(self, html: str, source_url: str, retrieved_at: datetime) -> RagDocument:
        soup = BeautifulSoup(html, "html.parser")
        title = self._extract_title(soup, source_url)
        tags = self._extract_categories(soup)
        links = self._extract_links(soup, source_url)
        namespace = self._infer_namespace(source_url, title)

        content = self._extract_main_content(soup)
        self._remove_noise(content)
        sections = self._extract_sections(content)

        return RagDocument(
            title=title,
            source_url=source_url,
            entity_type=self._infer_entity_type(tags, namespace, title),
            retrieved_at=retrieved_at,
            sections=sections,
            namespace=namespace,
            tags=tags,
            links=links,
        )

    def _extract_title(self, soup: BeautifulSoup, source_url: str) -> str:
        heading = soup.select_one("#firstHeading")
        if heading:
            return self._clean_text(heading.get_text(" ", strip=True))

        title = soup.select_one("title")
        if title:
            return self._clean_text(title.get_text(" ", strip=True).split("-")[0])

        return source_url.rstrip("/").rsplit("/", maxsplit=1)[-1].replace("_", " ")

    def _extract_categories(self, soup: BeautifulSoup) -> list[str]:
        categories: list[str] = []
        for anchor in soup.select("#catlinks a"):
            text = self._clean_text(anchor.get_text(" ", strip=True))
            if text and text.lower() != "categories":
                categories.append(text)
        return sorted(set(categories))

    def _extract_links(self, soup: BeautifulSoup, source_url: str) -> list[str]:
        links: set[str] = set()
        for anchor in soup.select("#mw-content-text a[href]"):
            href = anchor.get("href", "")
            if href.startswith(("#", "mailto:", "javascript:")):
                continue
            absolute = urljoin(source_url, href).split("#", maxsplit=1)[0]
            links.add(absolute)
        return sorted(links)

    def _extract_main_content(self, soup: BeautifulSoup) -> Tag:
        content = soup.select_one("#mw-content-text .mw-parser-output")
        if content is not None:
            return content

        fallback = soup.select_one("#mw-content-text") or soup.body
        if fallback is None:
            raise ValueError("Could not find main content in UESP page.")
        return fallback

    def _remove_noise(self, content: Tag) -> None:
        for selector in NOISE_SELECTORS:
            for element in content.select(selector):
                if self._is_live_tag(element):
                    element.decompose()

        for element in content.select("[style]"):
            if not self._is_live_tag(element):
                continue
            style = str(element.get("style", "")).replace(" ", "").lower()
            if "display:none" in style:
                element.decompose()

        for table in content.find_all("table"):
            if not self._is_live_tag(table):
                continue
            classes = set(table.get("class", []))
            if classes.intersection({"navbox", "metadata", "ambox", "notice"}):
                table.decompose()

    def _is_live_tag(self, tag: Tag) -> bool:
        return getattr(tag, "attrs", None) is not None

    def _extract_sections(self, content: Tag) -> list[RagSection]:
        sections: list[RagSection] = []
        current_heading = "Overview"
        current_level = 1
        current_parts: list[str] = []
        skip_current = False

        for child in content.children:
            if not isinstance(child, Tag):
                continue

            if self._is_heading(child):
                if current_parts and not skip_current:
                    sections.append(
                        self._build_section(current_heading, current_level, current_parts)
                    )

                current_heading = self._heading_text(child)
                current_level = int(child.name[1])
                current_parts = []
                skip_current = current_heading.lower() in LOW_VALUE_SECTION_HEADINGS
                continue

            if skip_current:
                continue

            markdown = self._element_to_markdown(child)
            if markdown:
                current_parts.append(markdown)

        if current_parts and not skip_current:
            sections.append(self._build_section(current_heading, current_level, current_parts))

        return sections

    def _build_section(
        self,
        heading: str,
        level: int,
        markdown_parts: list[str],
    ) -> RagSection:
        return RagSection(
            heading=heading,
            level=level,
            markdown=self._clean_markdown("\n\n".join(markdown_parts)),
        )

    def _is_heading(self, tag: Tag) -> bool:
        return tag.name in {"h2", "h3", "h4"}

    def _heading_text(self, tag: Tag) -> str:
        headline = tag.select_one(".mw-headline")
        text = headline.get_text(" ", strip=True) if headline else tag.get_text(" ", strip=True)
        return self._clean_text(text)

    def _element_to_markdown(self, tag: Tag) -> str:
        markdown = html_to_markdown(
            str(tag),
            heading_style="ATX",
            bullets="-",
            strip=["span"],
        )
        return self._clean_markdown(markdown)

    def _infer_namespace(self, source_url: str, title: str) -> str:
        page_name = unquote(urlparse(source_url).path.rsplit("/", maxsplit=1)[-1])
        candidate = page_name or title
        if ":" not in candidate:
            return "Main"
        return candidate.split(":", maxsplit=1)[0]

    def _infer_entity_type(self, tags: list[str], namespace: str, title: str) -> str:
        normalized = " ".join([*tags, namespace, title]).replace("-", " ").lower()
        for needles, entity_type in ENTITY_RULES:
            if any(needle in normalized for needle in needles):
                return entity_type
        if namespace.lower() == "lore":
            return "lore"
        return "page"

    def _clean_text(self, value: str) -> str:
        value = value.replace("[edit]", "")
        return re.sub(r"\s+", " ", value).strip()

    def _clean_markdown(self, markdown: str) -> str:
        markdown = markdown.replace("\xa0", " ")
        markdown = re.sub(r"\[edit\]", "", markdown, flags=re.IGNORECASE)
        markdown = re.sub(r"\n{3,}", "\n\n", markdown)
        markdown = re.sub(r"[ \t]+\n", "\n", markdown)
        return markdown.strip()
