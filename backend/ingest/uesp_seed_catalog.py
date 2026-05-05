from __future__ import annotations

from dataclasses import dataclass

from backend.ingest.mediawiki_client import MediaWikiClient, WikiPageCandidate


@dataclass(frozen=True)
class DiscoveryScope:
    name: str
    allowed_prefixes: tuple[str, ...]
    categories: tuple[str, ...]
    hubs: tuple[str, ...]


SKYRIM_GAMEPLAY_CATEGORIES = (
    "Skyrim-Quests",
    "Skyrim-Places",
    "Skyrim-People",
    "Skyrim-NPCs",
    "Skyrim-Creatures",
    "Skyrim-Items",
    "Skyrim-Weapons",
    "Skyrim-Armor",
    "Skyrim-Books",
    "Skyrim-Spells",
    "Skyrim-Factions",
    "Skyrim-Skills",
    "Skyrim-Shouts",
    "Skyrim-Ingredients",
    "Skyrim-Artifacts",
    "Skyrim-Dungeons",
    "Skyrim-Holds",
    "Skyrim-Cities",
    "Skyrim-Towns",
    "Skyrim-Settlements",
)

LORE_CATEGORIES = (
    "Lore",
    "Lore-People",
    "Lore-Places",
    "Lore-Books",
    "Lore-Creatures",
    "Lore-Deities",
    "Lore-Factions",
    "Lore-Races",
    "Lore-History",
    "Lore-Events",
    "Lore-Organizations",
    "Lore-Mythology",
    "Lore-Artifacts",
    "Lore-Magic",
)

SKYRIM_HUBS = (
    "Skyrim:Skyrim",
    "Skyrim:Quests",
    "Skyrim:Main_Quest",
    "Skyrim:Side_Quests",
    "Skyrim:Daedric_Quests",
    "Skyrim:Miscellaneous_Quests",
    "Skyrim:Places",
    "Skyrim:Holds",
    "Skyrim:Cities",
    "Skyrim:Dungeons",
    "Skyrim:People",
    "Skyrim:NPCs",
    "Skyrim:Creatures",
    "Skyrim:Items",
    "Skyrim:Weapons",
    "Skyrim:Armor",
    "Skyrim:Unique_Items",
    "Skyrim:Artifacts",
    "Skyrim:Books",
    "Skyrim:Spells",
    "Skyrim:Shouts",
    "Skyrim:Factions",
    "Skyrim:Skills",
    "Skyrim:Ingredients",
)

LORE_HUBS = (
    "Lore:Main_Page",
    "Lore:History",
    "Lore:Gods",
    "Lore:Daedra",
    "Lore:Aedra",
    "Lore:Races",
    "Lore:Nords",
    "Lore:Dragons",
    "Lore:Dragonborn",
    "Lore:Tamriel",
    "Lore:Skyrim",
    "Lore:Places",
    "Lore:Factions",
    "Lore:Books",
    "Lore:Artifacts",
    "Lore:Magic",
)

SCOPES: dict[str, DiscoveryScope] = {
    "skyrim": DiscoveryScope(
        name="skyrim",
        allowed_prefixes=("/wiki/Skyrim:",),
        categories=SKYRIM_GAMEPLAY_CATEGORIES,
        hubs=SKYRIM_HUBS,
    ),
    "all": DiscoveryScope(
        name="all",
        allowed_prefixes=("/wiki/Skyrim:", "/wiki/Lore:"),
        categories=SKYRIM_GAMEPLAY_CATEGORIES + LORE_CATEGORIES,
        hubs=SKYRIM_HUBS + LORE_HUBS,
    ),
}


def get_scope(name: str) -> DiscoveryScope:
    try:
        return SCOPES[name]
    except KeyError as exc:
        valid = ", ".join(sorted(SCOPES))
        raise ValueError(f"Unknown scope {name!r}. Valid scopes: {valid}") from exc


def iter_hub_candidates(
    scope: DiscoveryScope,
    client: MediaWikiClient,
) -> list[WikiPageCandidate]:
    candidates: list[WikiPageCandidate] = []
    for title in scope.hubs:
        candidates.append(
            WikiPageCandidate(
                title=title,
                url=client.title_to_url(title),
                source="hub",
                namespace=client.infer_namespace(title),
            )
        )
    return candidates
