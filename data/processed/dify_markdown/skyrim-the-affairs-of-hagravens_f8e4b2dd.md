---
source_url: "https://en.uesp.net/wiki/Skyrim:The_Affairs_of_Hagravens"
title: "Skyrim:The Affairs of Hagravens"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:33:00.192613+00:00"
tags: ["Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Special Edition Patch", "Skyrim-Quests", "Skyrim-Quests-Dungeon Quests", "Skyrim-Quests-Miscellaneous", "Skyrim-SRQRP-Requires Final Review"]
---

# Skyrim:The Affairs of Hagravens

## Overview

|  |  |
| --- | --- |
| **After discovering an [imprisoned hagraven](/wiki/Skyrim:Melka "Skyrim:Melka"), you must help her reclaim her lost tower.** | |

|  |  |
| --- | --- |
| Quest Giver: | [Melka](/wiki/Skyrim:Melka "Skyrim:Melka") |
| Location(s): | [Blind Cliff Cave](/wiki/Skyrim:Blind_Cliff_Cave "Skyrim:Blind Cliff Cave") |
| Reward: | [Eye of Melka](/wiki/Skyrim:Eye_of_Melka "Skyrim:Eye of Melka") |
| ID: | dunBlindCliffQST |
| Suggested Level: | 14 |

[![](//images.uesp.net/thumb/8/8c/SR-quest-The-Affairs-Of-Hagravens.jpg/200px-SR-quest-The-Affairs-Of-Hagravens.jpg)](/wiki/File:SR-quest-The-Affairs-Of-Hagravens.jpg)

Melka needs your help

## Quick Walkthrough

1. Find [Melka](/wiki/Skyrim:Melka "Skyrim:Melka") imprisoned in [Blind Cliff Cave](/wiki/Skyrim:Blind_Cliff_Cave "Skyrim:Blind Cliff Cave").
2. Protect her from [Forsworn](/wiki/Skyrim:Forsworn "Skyrim:Forsworn") as you travel through the tower.
3. Kill [Petra](/wiki/Skyrim:Petra "Skyrim:Petra").

### A Hagraven in Need

Upon entering [Blind Cliff Bastion](/wiki/Skyrim:Blind_Cliff_Bastion "Skyrim:Blind Cliff Bastion") you will see the hagraven [Melka](/wiki/Skyrim:Melka "Skyrim:Melka") in a cage. As you approach her, she will ask you to free her and help her reclaim her tower from another hagraven, [Petra](/wiki/Skyrim:Petra "Skyrim:Petra"). To release Melka, pull the chain near the cage. After leaving the cage she will then lead you through her tower. The first room displays a central stone slab adorned with three handles; Melka will tell you that the middle one is the correct one to use. Pull the handle and go through the gate it opens. Follow the short path into a room inhabited by a [Forsworn](/wiki/Skyrim:Forsworn "Skyrim:Forsworn"). There will then be a gate with a tunnel full of [swinging blades](/wiki/Skyrim:Swinging_Blades "Skyrim:Swinging Blades"). Melka will mention a lever that will stop the blades: she will then pull a handle on the floor that lowers a section of a wall, revealing another lever to do just that.

### Reclaiming the Tower

Move through the tunnel and go up the stairs. After the stairs you will pass a section of wall that moves away when the nearby handle is pulled. Through the newly cleared section of wall are some ingots and a chest. The next room has an [alchemy lab](/wiki/Skyrim:Alchemy_Lab "Skyrim:Alchemy Lab"), and is referred to by Melka as her "parlor". Follow the path past the quicksilver ore. The next room contains Petra and two Forsworn. Killing them and Petra will result in Melka rewarding you with the unique staff, [Eye of Melka](/wiki/Skyrim:Eye_of_Melka "Skyrim:Eye of Melka"). If Melka died anywhere along the way you can simply loot the staff from her corpse.

## Notes

- You can also just kill Melka for the staff, but you will still have the objective to kill Petra and you will have lost your guide.
- If you run ahead of Melka (or she gets stuck somewhere and halts long enough), it is possible to kill Petra, complete the quest, leave the dungeon, and not obtain the staff by talking to Melka and demanding a reward. Though rare, this can result in a bug where Melka randomly shows up wherever you are to talk to you, as the quest objective of her being scripted by her AI package to move to you, force-greet and engage in dialogue (dunBlindCliffForceGreetAndRewardPlayer) has not been completed.

## Bugs

- If you kill Petra before freeing Melka, the quest does not complete and remains in your list of quests.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.3.1, addresses this issue. This fix later got reworked in Version 4.2.4 due to a previously faulty stage check.
- Completing this quest counts towards the [Sideways](/wiki/Skyrim:Sideways "Skyrim:Sideways") [achievement](/wiki/Skyrim:Achievements "Skyrim:Achievements"), even though it is not a [Side Quest](/wiki/Skyrim:Side_Quests "Skyrim:Side Quests"), i.e., it does not have a separate entry in your quest log

  **Mod Notes**: Quest stage 100 of the quest calls AchievementsQuest.IncSideQuests(), even though the quest Type is "Miscellaneous" instead of "Side Quests"

  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.4, fixes this bug.
- The quest might not properly complete its objectives due to the quest checking a wrong prerequisite stage upon the death of either Petra or Melka.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.1.4, fixes this bug.

## Quest Stages

| The Affairs of Hagravens (dunBlindCliffQST) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 15 |  | *Objective 15:* Kill the Hagraven Petra |
| 20 |  | *Objective 15:* Kill the Hagraven Petra |
| 100 | ☑ |  |
| 200 |  | The Hagraven Melka is dead. |

- The following empty quest stages were omitted from the table: 10, 11, 30, 40, 45, 50, 60, 256.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage dunBlindCliffQST stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest dunBlindCliffQST`.
