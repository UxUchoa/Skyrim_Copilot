---
source_url: "https://en.uesp.net/wiki/Skyrim:Hunting_the_Monster"
title: "Skyrim:Hunting the Monster"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:40:26.786421+00:00"
tags: ["MetaTemplate-Load", "Skyrim-Bugs Fixed by the Unofficial Skyrim Legendary Edition Patch", "Skyrim-Dawnguard", "Skyrim-Dawnguard-Confirmed Bugs", "Skyrim-Dawnguard-Quests", "Skyrim-Dawnguard-Quests-Dawnguard", "Skyrim-Quests", "Skyrim-Quests-Radiant", "Skyrim-SRQRP-Requires Final Review"]
---

# Skyrim:Hunting the Monster

## Overview

|  |  |
| --- | --- |
| [SR-qico-Dawnguard Dawnguard.png](/wiki/File:SR-qico-Dawnguard_Dawnguard.png) | **Destroy the [vampire](/wiki/Skyrim:Vampire "Skyrim:Vampire") target.** |

|  |  |
| --- | --- |
| Quest Giver: | [Gunmar](/wiki/Skyrim:Gunmar "Skyrim:Gunmar") |
| Location(s): | Radiant City; Radiant [Bandit Camp](/wiki/Category:Skyrim-Places-Bandit_Camps "Category:Skyrim-Places-Bandit Camps") or [Warlock Lair](/wiki/Category:Skyrim-Places-Warlock_Lairs "Category:Skyrim-Places-Warlock Lairs") |
| Reward: | Leveled enchanted item |
| ID: | DLC1RH04 |

[![](//images.uesp.net/thumb/5/52/SR-quest-Hunting_the_Monster.jpg/200px-SR-quest-Hunting_the_Monster.jpg)](/wiki/File:SR-quest-Hunting_the_Monster.jpg)

Follow the trail to the vampire...

## Quick Walkthrough

1. Speak with [Gunmar](/wiki/Skyrim:Gunmar "Skyrim:Gunmar") in [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard").
2. Learn of the [vampire's](/wiki/Skyrim:Vampire "Skyrim:Vampire") whereabouts.
3. Destroy the vampire at the hideout.
4. Report back to Gunmar.

## Detailed Walkthrough

Speak with [Gunmar](/wiki/Skyrim:Gunmar "Skyrim:Gunmar") in [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard") and tell him you are ready to offer some help. He has learned of a possible monster. However, he doesn't know its exact whereabouts and will suggest you pay a visit to the [vampire's](/wiki/Skyrim:Vampire "Skyrim:Vampire") last known contact to glean more information. The vampire's friend will be a notable of a random city (though not a [jarl](/wiki/Skyrim:Jarl "Skyrim:Jarl")).

Once you've found the friend, you will need to extract some information about the vampire's location by either [pickpocketing](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") the letter they are carrying, or pass a speech check (you'll require a [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") skill of at least 50).

| Option | Dialogue | | | | Reaction |
| --- | --- | --- | --- | --- | --- |
| Make this easier for you, tell me what I want to know. **(Persuade)** | **Passed**: All right... Here, take this. **Failed**: Like I said. I don't know what you're talking about. | | | | **Passed**: Get the location **Failed**: Nothing |
| Perhaps some coin will jog your memory? **(Bribe)** | **Passed**: Well... we weren't the closest of friends... Here, take this. **Failed**: Afraid my memory can't be bought with what you've got there. | | | | **Passed**: Get the location **Failed**: Nothing |
| I'll get rough with you if I have to. **(Intimidate)** | **Passed**: All right, calm down... Here, take this. **Failed**: You don't scare me. **Or** You don't scare me. Let's go. **(Brawl)** | | | | **Passed**: Get the location **Failed**: Nothing |

If you're successful, you will receive a *[Letter from the Vampire](/wiki/Skyrim:Letter_from_the_Vampire "Skyrim:Letter from the Vampire")* containing the fiend's location, which will be immediately marked on your map. It will be a random (non-quest related) [bandit camp](/wiki/Category:Skyrim-Places-Bandit_Camps "Category:Skyrim-Places-Bandit Camps") or [warlock lair](/wiki/Category:Skyrim-Places-Warlock_Lairs "Category:Skyrim-Places-Warlock Lairs") with a boss enemy.

Travel to the location and eliminate your target. You won't need to kill all other enemies to complete the quest, although in practice you often won't have much choice. Once the vampire is slain, return to Gunmar for your reward: a leveled enchanted item.

## Notes

- If [Dragonborn](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") is installed, some radiant locations may be on [Solstheim](/wiki/Skyrim:Solstheim "Skyrim:Solstheim"). If you are in Skyrim, you will not receive a quest marker pointing you to the quest location, but must travel to Solstheim first (at which point any quest markers you have to quests in Skyrim will disappear).
- This quest can be repeated infinitely. After you have destroyed the target vampire, you can be sent to take care of another by taking the quest again.

## Bugs

- If the letter directs you to [Ansilvund](/wiki/Skyrim:Ansilvund "Skyrim:Ansilvund"), and [Lu'ah](/wiki/Skyrim:Lu%27ah_Al-Skaven "Skyrim:Lu'ah Al-Skaven") is already dead, there will be no boss in the dungeon and no quest marker leading you to a target.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") The only way to progress the quest is with the console command `setstage DLC1RH04 100`.
- An intimidation topic option during this quest may not have the brawl quest property defined, resulting in a broken call to the brawling system.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch"), version 3.0.1, fixes this bug.

## Quest Stages

| Hunting the Monster (DLC1RH04) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 10 |  | Gunmar has sent me to <Alias=Habitation> where I am to learn the current whereabouts of the <Alias=Vampire>. I will learn this through interrogation of his last known contact <Alias=Friend>, or searching for evidence. Once its location is obtained, I am to destroy the beast in its lair. *Objective 10:* Find evidence of the vampire's whereabouts |
| 50 |  | Gunmar has sent me to <Alias=Habitation> where I have learned from <Alias=Friend> the whereabouts of the <Alias=Vampire>. I am now to journey to <Alias=Dungeon> and destroy the beast. *Objective 50:* Kill the <Alias=Vampire> at <Alias=Dungeon> |
| 100 |  | *Objective 100:* Return to Gunmar |
| 255 | ☑ | Gunmar sent me to <Alias=Habitation> where I have learned from <Alias=Friend> the whereabouts of the <Alias=Vampire>. I then journeyed to <Alias=Dungeon> and destroyed the beast. |

- The following empty quest stages were omitted from the table: 0, 1, 20, 51.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage DLC1RH04 stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest DLC1RH04`.
