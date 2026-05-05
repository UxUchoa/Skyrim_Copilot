---
source_url: "https://en.uesp.net/wiki/Skyrim:Dragon_Research"
title: "Skyrim:Dragon Research"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:37:33.901787+00:00"
tags: ["All Pages Needing Verification", "All Stubs", "Skyrim-Bugs Fixed by the Official Skyrim Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Pages Needing Verification", "Skyrim-Quest Stubs", "Skyrim-Quests", "Skyrim-Quests with Incorrectly Named Images", "Skyrim-Quests-Miscellaneous", "Skyrim-SRQRP-Reward Checked", "Skyrim-SRQRP-Reward Written", "Skyrim-SRQRP-Walkthrough Not Checked", "Skyrim-SRQRP-Walkthrough Written", "Skyrim-Stubs"]
---

# Skyrim:Dragon Research

## Overview

|  |
| --- |
| **This page is currently being rewritten as part of the [Skyrim Quest Redesign Project](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project "UESPWiki:Skyrim Quest Redesign Project").** The page is being rewritten and checked in several stages. All users are welcome to make changes to the page. If you make a change that is relevant to the project, please update this template accordingly, and make sure you have observed the [project guidelines](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project#Guidelines "UESPWiki:Skyrim Quest Redesign Project").  Details  **Walkthrough**: written by [125.79.102.141](/wiki/Special:Contributions/125.79.102.141 "Special:Contributions/125.79.102.141"), *not checked*  **Reward**: written by multiple users, checked by [RobinHood70](/wiki/User:RobinHood70 "User:RobinHood70") |

|  |  |
| --- | --- |
| **Help [Esbern](/wiki/Skyrim:Esbern "Skyrim:Esbern") complete his research on [dragons](/wiki/Skyrim:Dragon "Skyrim:Dragon").** | |

|  |  |
| --- | --- |
| Location(s): | None |
| Reward: | [Esbern's Potion](/wiki/Skyrim:Esbern%27s_Potion "Skyrim:Esbern's Potion") |
| ID: | FreeformSkyHavenTempleD |
| --- | |
| |  |  | | --- | --- | | **← Previous** [Dragon Hunting](/wiki/Skyrim:Dragon_Hunting "Skyrim:Dragon Hunting") |  | | |
| |  |  | | --- | --- | | ← Previous | [Dragon Hunting](/wiki/Skyrim:Dragon_Hunting "Skyrim:Dragon Hunting") | | |

[![](//images.uesp.net/thumb/9/9f/SR-creature-Dragon_Dead.jpg/200px-SR-creature-Dragon_Dead.jpg)](/wiki/File:SR-creature-Dragon_Dead.jpg)

Now for the harvest

## Quick Walkthrough

- Speak with [Esbern](/wiki/Skyrim:Esbern "Skyrim:Esbern").
- Acquire a [dragon bone](/wiki/Skyrim:Dragon_Bone "Skyrim:Dragon Bone") and a [dragon scale](/wiki/Skyrim:Dragon_Scales "Skyrim:Dragon Scales").
- Return to Esbern.
- Drink the [potion](/wiki/Skyrim:Esbern%27s_Potion "Skyrim:Esbern's Potion").
- Speak with Esbern once more to complete the quest.

## Detailed Walkthrough

Once you have three followers recruited as [Blades](/wiki/Skyrim:Blades "Skyrim:Blades"), you can ask [Esbern](/wiki/Skyrim:Esbern "Skyrim:Esbern") for [dragons](/wiki/Skyrim:Dragon "Skyrim:Dragon") to kill. Once you agree to kill one, Esbern will send you to a random place where you'll find a dragon. After you kill the dragon, you'll get the update to the quest stating "Return to Esbern". Return and speak to him; he'll ask for a [dragon bone](/wiki/Skyrim:Dragon_Bone "Skyrim:Dragon Bone") and a [dragon scale](/wiki/Skyrim:Dragon_Scales "Skyrim:Dragon Scales"). Give him the dragon bone and scale and he'll give you a [potion](/wiki/Skyrim:Esbern%27s_Potion "Skyrim:Esbern's Potion"). Drink the potion to gain the [Dragon Infusion](/wiki/Skyrim:Dragon_Infusion "Skyrim:Dragon Infusion") perk. Speak with him once more to complete the quest. The potion adds the permanent perk of 25% less melee damage from dragons.

## Bugs

- You do not gain the perk after drinking the potion and it is not obtainable via normal gameplay means.
  - The [Official Skyrim Patch](/wiki/Skyrim:Patch "Skyrim:Patch"), version 1.9, fixes this bug.
- The quest journal entry won't update after quest completion.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.0, fixes this bug.
  - [![On PlayStation](//images.uesp.net/6/64/Playstation.svg)](/wiki/Skyrim:PlayStation "Skyrim:PlayStation")[![On Xbox](//images.uesp.net/3/33/Xbox.svg)](/wiki/Skyrim:Xbox "Skyrim:Xbox") If you don't want an uncompleted quest stuck in their quest log, you have the opportunity to back out of dialogue with Esbern after the 'Talk to Esbern' objective but before you inquire about a dragon location. Note: This bug does not appear to be present in the Anniversary Edition.[*verification needed — how is this affected by the [Paarthurnax](/wiki/Skyrim:Paarthurnax_(quest) "Skyrim:Paarthurnax (quest)") quest?*]
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") **Workaround** - Basically, you must *not* give the dragon's bone and scale to Esbern; use console commands instead. There are three contexts to consider, each with its own solution: the first one is before returning to Esbern, the second one is before turning-in the dragon's scale and bone asked by Esbern, and the third one is after getting the potion (after giving the dragon's scale and bone).
    - **Before returning to Esbern** - You killed the dragon and got a new journal entry stating "Return to Esbern". Use the console to add the perk : `player.addspell 000F5FFA`. From then on, you won't be asked to retrieve a dragon's scale and bones and thus won't receive the resulting potion (it seems that one condition for triggering the quest is set by detecting that you don't have the perk yet).
    - **Before turning-in a dragon's scale and bone (recommended)** - You've returned to Esbern and told him that the dragon is dead, which triggered a new quest requiring a dragon's bone and scale. In the console, type:

      :   ```
          player.addspell 000F5FFA
          SetObjectiveCompleted FreeFormSkyHavenTempleD 10 1
          ```
    - **After giving bone and scale to Esbern** - The quest has already been started and it's supposed to be completed, but the journal entry is still there : you've given the dragon's bone and scale and thus received the potion, however without any effect after you drank it since it has a bug (no perk imbued). You must first reset the quest so as to start it over again, then add the perk to your powers, and finally clear the entry from your journal with the quest set as "completed". In the console, type:

      :   ```
          ResetQuest FreeFormSkyHavenTempleD
          SetStage FreeFormSkyHavenTempleD 10
          player.addspell 000F5FFA
          SetObjectiveCompleted FreeFormSkyHavenTempleD 10 1
          ```
    - **How to fix/finish this quest?** - Set quest as "completed". In the console, type:

      :   ```
          SetStage FreeFormSkyHavenTempleD 100
          ```
- You can get Esbern's Potion quest line without recruiting any Blades. However, it will not be titled "Dragon Research" and is located in Miscellaneous Quests. After completing Alduin's Wall (also may happen before you even visit Esbern), killing a dragon at a defined radiant location (such as a word wall) will trigger the objective "Return to Esbern". Speaking to Esbern then triggers "Give a Dragon Scale and a Dragon Bone to Esbern". When you give them to him, he will give you Esbern's Potion.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.5, fixes this bug.

## Quest Stages

| Dragon Research (FreeformSkyHavenTempleD) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 10 |  | *Objective 10:* Bring a Dragon Scale and a Dragon Bone to Esbern |

- The following empty quest stages were omitted from the table: 100.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage FreeformSkyHavenTempleD stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest FreeformSkyHavenTempleD`.

![](//images.uesp.net/thumb/4/45/SR-achievement-Platinum_Trophy.png/32px-SR-achievement-Platinum_Trophy.png)

*This [Skyrim](/wiki/Skyrim:Skyrim "Skyrim:Skyrim")-related article is a [stub](/wiki/UESPWiki:Stub "UESPWiki:Stub"). You can help by [expanding it](https://en.uesp.net/w/index.php?title=Skyrim:Dragon_Research&action=edit).*
