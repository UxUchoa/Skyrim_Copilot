---
source_url: "https://en.uesp.net/wiki/Skyrim:An_enemy's_gratitude"
title: "Skyrim:An enemy's gratitude"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:38:11.767978+00:00"
tags: ["All Pages Needing Images", "Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Special Edition Patch", "Skyrim-Confirmed Bugs", "Skyrim-Quest Pages Needing Images", "Skyrim-Quests", "Skyrim-Quests-Radiant", "Skyrim-Quests-World Interactions", "Skyrim-SRQRP-Reward Not Checked", "Skyrim-SRQRP-Reward Written", "Skyrim-SRQRP-Walkthrough Checked", "Skyrim-SRQRP-Walkthrough Written", "Skyrim-Unconfirmed Bugs"]
---

# Skyrim:An enemy's gratitude

## Overview

|  |
| --- |
| **This page is currently being rewritten as part of the [Skyrim Quest Redesign Project](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project "UESPWiki:Skyrim Quest Redesign Project").** The page is being rewritten and checked in several stages. All users are welcome to make changes to the page. If you make a change that is relevant to the project, please update this template accordingly, and make sure you have observed the [project guidelines](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project#Guidelines "UESPWiki:Skyrim Quest Redesign Project").  Details  **Walkthrough**: written by multiple users, checked by [Riliane](/wiki/User:Riliane "User:Riliane")  **Reward**: written by [RobinHood70](/wiki/User:RobinHood70 "User:RobinHood70"), *not checked* |

|  |
| --- |
| **This article could benefit from an image**. See [Help:Images](/wiki/Help:Images "Help:Images") for information on how to upload images. Please remove this template from the page when finished. |

|  |  |
| --- | --- |
| **Experience the rewards for killing someone.** | |

|  |  |
| --- | --- |
| Location(s): | None |
| Reward: | 50-200 gold (see below) |
| ID: | WIKill04 |

## Quick Walkthrough

1. Kill an NPC.
2. Receive a letter from a [courier](/wiki/Skyrim:Courier "Skyrim:Courier").
3. *(Conditional)* Visit the letter's sender for a reward.

## Detailed Walkthrough

When you kill a person, it is possible you will be given a message from a [courier](/wiki/Skyrim:Courier "Skyrim:Courier") from that person's enemy, claiming that they hated the person too and are glad you took care of them. If the [relationship](/wiki/Skyrim:Disposition "Skyrim:Disposition") between the enemy and the victim was foe or worse, the person thanking you will request that you visit them for a reward through a [reward letter](/wiki/Skyrim:WIKill04RewardLetter "Skyrim:WIKill04RewardLetter"). Otherwise, they'll just send you a [letter of thanks](/wiki/Skyrim:WIKill04ThanksLetter "Skyrim:WIKill04ThanksLetter").

The reward is 50 gold for each [relationship rank](/wiki/Skyrim:Disposition#Relationship_Rank "Skyrim:Disposition") below zero.

## Notes

- Rich enemies were supposed to give a reward of 200 gold per rank, but no NPCs in the game are flagged as rich.
- Version 4.3.7 of the [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch") changes the letter's font to the handwritten font.

## Bugs

- It is possible for the Dragonborn to receive a letter from themselves, rendering it impossible to complete the quest normally.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.3, fixes this bug. ([details](https://afktrack.afkmods.com/index.php?a=issues&i=28980))
- It is possible for the person giving the reward to be killed and thus cause the quest to get stuck because you can no longer collect.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.4, fixes this bug. ([details](https://afktrack.afkmods.com/index.php?a=issues&i=29128))
- If the relationship between enemy and victim is -3 (enemy) or worse, the reward letter will be delivered, but the objective to collect the reward will not be given.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.5, fixes this bug.
- If letter is placed on a bookshelf may become blank and render the reward unobtainable.
- It's possible to get the letter even if you killed the enemy "in disguise", such as being transformed into a Werewolf or Vampire Lord, where NPCs aren't supposed to recognize you. **?**

## Quest Stages

| An enemy's gratitude (WIKill04) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 1 |  | *Objective 1:* Read the letter from <Alias=Enemy> |
| 10 |  | *Objective 10:* Collect the reward from <Alias=Enemy> for killing <Alias=Victim> *(conditional on relationship rank)* |

- The following empty quest stages were omitted from the table: 0, 100.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage WIKill04 stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest WIKill04`.
