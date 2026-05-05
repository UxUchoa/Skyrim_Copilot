---
source_url: "https://en.uesp.net/wiki/Skyrim:Bounty_Collector"
title: "Skyrim:Bounty Collector"
entity_type: "npc"
namespace: "Skyrim"
retrieved_at: "2026-05-05T00:16:09.096783+00:00"
tags: ["MetaTemplate-Load", "Skyrim-Bandit", "Skyrim-Bugs Fixed by the Unofficial Skyrim Special Edition Patch", "Skyrim-Confirmed Bugs", "Skyrim-Factions-WEBountyHunter", "Skyrim-Leveled NPCs", "Skyrim-Male NPCs", "Skyrim-NPCs", "Skyrim-NPCs-World Interactions", "Skyrim-No Crime", "Skyrim-Nord", "Skyrim-Nord-Male", "Skyrim-Voice-MaleNord"]
---

# Skyrim:Bounty Collector

## Overview

| Bounty Collector | | | |
| --- | --- | --- | --- |
| Race | [Nord](/wiki/Skyrim:Nord "Skyrim:Nord") | Gender | Male |
| Level | Radiant (6-28) | Class | [Bandit](/wiki/Skyrim:Bandit_(class) "Skyrim:Bandit (class)") |
| [RefID](/wiki/Skyrim:NPCs#Console_IDs "Skyrim:NPCs") | N/A | [BaseID](/wiki/Skyrim:NPCs#Console_IDs "Skyrim:NPCs") | 000F812A |
| Other Information | | | |
| [Health](/wiki/Skyrim:Health "Skyrim:Health") | Radiant (155-497) | | |
| [Magicka](/wiki/Skyrim:Magicka "Skyrim:Magicka") | Radiant (25-40) | | |
| [Stamina](/wiki/Skyrim:Stamina "Skyrim:Stamina") | Radiant (95-258) | | |
| [Morality](/wiki/Skyrim:Morality "Skyrim:Morality") | No Crime | [Aggression](/wiki/Skyrim:Aggression "Skyrim:Aggression") | Very Aggressive |
| Voice Type | [MaleNord](/wiki/Category:Skyrim-Voice-MaleNord "Category:Skyrim-Voice-MaleNord") | | |
| [Faction(s)](/wiki/Skyrim:Factions "Skyrim:Factions") | [WEBountyHunter](/wiki/Skyrim:WEBountyHunter "Skyrim:WEBountyHunter") | | |

[![](//images.uesp.net/thumb/0/0a/SR-npc-Bounty_Collector.jpg/200px-SR-npc-Bounty_Collector.jpg)](/wiki/File:SR-npc-Bounty_Collector.jpg)

Bounty Collector

A **Bounty Collector** can be [randomly encountered](/wiki/Skyrim:World_Interactions#Bounty_Collector "Skyrim:World Interactions") in the wilderness if you have accumulated a [bounty](/wiki/Skyrim:Crime#Bounties "Skyrim:Crime") of more than 1000 gold in any [hold](/wiki/Skyrim:Holds "Skyrim:Holds"). Unlike city [guards](/wiki/Skyrim:Guards "Skyrim:Guards"), he will ignore the distinction between holds and will attempt to track you down regardless of which hold you are in. He will demand from you payment equal to 1.2× your current bounty. If you refuse, he will attack.

He wears a set of leveled [heavy armor](/wiki/Skyrim:Heavy_Armor_(item) "Skyrim:Heavy Armor (item)") (up to [steel plate](/wiki/Skyrim:Steel_Plate "Skyrim:Steel Plate") in quality), including the boots, gauntlets, and helmet. He always carries at least one leveled [heavy shield](/wiki/Skyrim:Armor#Shields_2 "Skyrim:Armor") (up to [ebony](/wiki/Skyrim:Ebony "Skyrim:Ebony") in quality), a [dagger](/wiki/Skyrim:Dagger "Skyrim:Dagger") (up to [elven](/wiki/Skyrim:Elven "Skyrim:Elven") in quality), and 50-250 gold, dependent on his level. He will also carry either a leveled [one-handed weapon](/wiki/Skyrim:One-Handed_Weapons "Skyrim:One-Handed Weapons") or a leveled [two-handed weapon](/wiki/Skyrim:Two-Handed_Weapons "Skyrim:Two-Handed Weapons") (up to [ebony](/wiki/Skyrim:Ebony "Skyrim:Ebony") in quality).

## Dialogue

When he sees you in the wilderness, he will approach you and will tell you not to move:

:   *"Stop right there."*
:   **What do you want?**
:   *"You have quite the bounty on your head in [hold]. You pay me, and I see that your name is cleared."*

:   :   **I don't have the gold.**
    :   *"Then you are worth more to me dead!"* **(Becomes hostile)**

:   :   **Pay (Gold).**
    :   *"I will make sure this gets back to the Jarl. Minus my cut, of course. Consider your name cleared, for now."*

If you speak to him after handing over the gold, he will tell you:

:   *"I have no more business with you."*
:   *"People think they can run away from their crimes, but I will always catch up with them and make them pay."*

## Notes

- If you have the [Dragonborn](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") add-on installed, the bounty collector, like other high-level NPCs that use the same template, may be wearing [Nordic carved armor](/wiki/Skyrim:Nordic_Carved_Armor "Skyrim:Nordic Carved Armor").

## Bugs

- Paying the bounty collector may fail to clear your bounty.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") Find a guard for the hold you have the bounty in, open the [console](/wiki/Skyrim:Console "Skyrim:Console"), click on the guard, and use the command `paycrimegold 0 0` to pay off your bounty. Make sure you are close enough to the guard that his proper [RefID](/wiki/Skyrim:Form_ID#RefID.2C_BaseID "Skyrim:Form ID") appears when you click on him, or else the command won't work.
- Rather than approach you and demand payment, the bounty collector may simply attack you instead.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") Open the console, click on the bounty collector (his RefID will appear, with 'ff' as the first two digits), then type `scaonactor` followed by <enter>. This will remove his aggression towards you and start his normal dialogue about clearing your bounty.
- The bounty collector may charge you 0 gold in Falkreath Hold due to a typo in the script.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.1.5, fixes this bug.
