---
source_url: "https://en.uesp.net/wiki/Skyrim:Bounty:_Giant"
title: "Skyrim:Bounty: Giant"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:35:08.214589+00:00"
tags: ["Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Quests", "Skyrim-Quests-Miscellaneous-Bounty Quests", "Skyrim-Quests-Radiant", "Skyrim-SRQRP-Requires Final Review"]
---

# Skyrim:Bounty: Giant

## Overview

|  |  |
| --- | --- |
| **Kill a problematic [giant](/wiki/Skyrim:Giant "Skyrim:Giant") for a bounty reward.** | |

|  |  |
| --- | --- |
| Location(s): | None |
| Reward: | 100 gold |
| ID: | BQ03 |
| Required Level: | 20 |

[![](//images.uesp.net/thumb/f/fd/SR-quest-Bounty_Giant.jpg/200px-SR-quest-Bounty_Giant.jpg)](/wiki/File:SR-quest-Bounty_Giant.jpg)

Giants are troubling the Jarl's hold.

## Radiant Options

Any innkeeper, [Jarl](/wiki/Skyrim:Jarl "Skyrim:Jarl") or Jarl's [steward](/wiki/Skyrim:Steward "Skyrim:Steward") can give you this quest. You will be directed to one of the [giant camps](/wiki/Skyrim:Giant_Camps "Skyrim:Giant Camps") in the hold, where you will then need to kill a [giant](/wiki/Skyrim:Giant "Skyrim:Giant") there to obtain your reward from the jarl or steward of the hold.

| [Eastmarch](/wiki/Skyrim:Eastmarch "Skyrim:Eastmarch") | [Falkreath Hold](/wiki/Skyrim:Falkreath_Hold "Skyrim:Falkreath Hold") | [Hjaalmarch](/wiki/Skyrim:Hjaalmarch "Skyrim:Hjaalmarch") | [The Pale](/wiki/Skyrim:The_Pale "Skyrim:The Pale") | [Whiterun Hold](/wiki/Skyrim:Whiterun_Hold "Skyrim:Whiterun Hold") |
| --- | --- | --- | --- | --- |
| [Broken Limb Camp](/wiki/Skyrim:Broken_Limb_Camp "Skyrim:Broken Limb Camp") [Cradlecrush Rock](/wiki/Skyrim:Cradlecrush_Rock "Skyrim:Cradlecrush Rock") [Steamcrag Camp](/wiki/Skyrim:Steamcrag_Camp "Skyrim:Steamcrag Camp") | [Secunda's Kiss](/wiki/Skyrim:Secunda%27s_Kiss "Skyrim:Secunda's Kiss")[†](#intnote_secunda) | [Talking Stone Camp](/wiki/Skyrim:Talking_Stone_Camp "Skyrim:Talking Stone Camp") | [Blizzard Rest](/wiki/Skyrim:Blizzard_Rest "Skyrim:Blizzard Rest") [Red Road Pass](/wiki/Skyrim:Red_Road_Pass "Skyrim:Red Road Pass") [Stonehill Bluff](/wiki/Skyrim:Stonehill_Bluff "Skyrim:Stonehill Bluff") [Tumble Arch Pass](/wiki/Skyrim:Tumble_Arch_Pass "Skyrim:Tumble Arch Pass") | [Bleakwind Basin](/wiki/Skyrim:Bleakwind_Basin "Skyrim:Bleakwind Basin") [Guldun Rock](/wiki/Skyrim:Guldun_Rock "Skyrim:Guldun Rock") [Sleeping Tree Camp](/wiki/Skyrim:Sleeping_Tree_Camp "Skyrim:Sleeping Tree Camp") |

[†](#note_secunda)This location appears as "Secunda's Shelf" in your quest log.

## Quick Walkthrough

1. Get the bounty letter from an innkeeper, Jarl, or steward.
2. Go to the giant camp and kill the giant.
3. Return to the Jarl or the Jarl's steward for the reward.

## Detailed Walkthrough

Speaking with any innkeeper, Jarl, or Jarl's steward about work may lead them to give you a [letter of bounty](/wiki/Skyrim:Bounty_(giant) "Skyrim:Bounty (giant)") requesting you to kill a giant. This will give you a miscellaneous objective to kill the giant in a specific camp. Head to the camp specified in the letter and kill the marked giant (there may be multiple giants, but you only have to kill the marked one). Once the giant is killed, you can return to the Jarl or steward for your 100 gold reward.

## Notes

- Sometimes the Jarl may request to kill another giant in a camp previously cleared. This is not a bug. New giants will be spawned and will be correctly associated with markers, killing and quest updates.

## Bugs

- The objective "Collect bounty from Skald" may not clear from quest list. This bug is due to the quest pointer completing stage 100 when you talk to Skald instead of stage 101.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.0, fixes this bug.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") A possible workaround is to use the [console](/wiki/Skyrim:Console "Skyrim:Console") command `setObjectiveCompleted BQ03 101 1` before turning in the quest to Skald, to clear the journal entry. Then just talk to Skald to get your bounty.

## Quest Stages

| Bounty: Giant (BQ03) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 10 |  | *Objective 10:* Kill the giant located at <Alias=BountyLocation> |
| 100 |  | *Objective 100:* Collect bounty from <Alias=Steward>  *Objective 101:* Collect bounty from <Alias=Jarl> |

- The following empty quest stages were omitted from the table: 0, 200.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage BQ03 stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest BQ03`.
