---
source_url: "https://en.uesp.net/wiki/Skyrim:The_Fishing_Job"
title: "Skyrim:The Fishing Job"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:39:06.313286+00:00"
tags: ["Skyrim-Confirmed Bugs", "Skyrim-Quests", "Skyrim-Quests-Radiant", "Skyrim-Quests-Thieves Guild", "Skyrim-Quests-Thieves Guild-Radiant", "Skyrim-SRQRP-Reward Checked", "Skyrim-SRQRP-Reward Written", "Skyrim-SRQRP-Walkthrough Not Checked", "Skyrim-SRQRP-Walkthrough Written", "Skyrim-Unconfirmed Bugs"]
---

# Skyrim:The Fishing Job

## Overview

|  |
| --- |
| **This page is currently being rewritten as part of the [Skyrim Quest Redesign Project](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project "UESPWiki:Skyrim Quest Redesign Project").** The page is being rewritten and checked in several stages. All users are welcome to make changes to the page. If you make a change that is relevant to the project, please update this template accordingly, and make sure you have observed the [project guidelines](/wiki/UESPWiki:Skyrim_Quest_Redesign_Project#Guidelines "UESPWiki:Skyrim Quest Redesign Project").  Details  **Walkthrough**: written by multiple users, *not checked*  **Reward**: written by [Dwarfmp](/wiki/User:Dwarfmp "User:Dwarfmp"), checked by [Riliane](/wiki/User:Riliane "User:Riliane") |

|  |  |
| --- | --- |
| [SR-qico-Thieves Guild.png](/wiki/File:SR-qico-Thieves_Guild.png) | **Steal an item out of a target's pocket.** |

|  |  |
| --- | --- |
| Quest Giver: | [Delvin Mallory](/wiki/Skyrim:Delvin_Mallory "Skyrim:Delvin Mallory") in the [Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") |
| Location(s): | None |
| Reward: | [Leveled Gold](#Reward) |
| ID: | TGRGF |

[![](//images.uesp.net/thumb/7/70/SR-quest-The_Fishing_Job.jpg/200px-SR-quest-The_Fishing_Job.jpg)](/wiki/File:SR-quest-The_Fishing_Job.jpg)

A thief about to go "fishing"

## Quick Walkthrough

1. Talk to [Delvin Mallory](/wiki/Skyrim:Delvin_Mallory "Skyrim:Delvin Mallory") in [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") about "fishing jobs".
2. [Pick](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") the target's pocket to obtain the required items.
3. Return to Delvin.

## Detailed Walkthrough

After joining the Thieves Guild, Delvin Mallory will tell you that he handles all the fishing, [numbers](/wiki/Skyrim:The_Numbers_Job "Skyrim:The Numbers Job") and [bedlam](/wiki/Skyrim:The_Bedlam_Job "Skyrim:The Bedlam Job") jobs, with "fishing" being a euphemism for [picking](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") someone's pockets. Ask him for a "fishing" job and he will give you a target and tell you to steal a particular item from them.

The item that needs to be stolen is a randomly-selected [gem](/wiki/Skyrim:Gems "Skyrim:Gems") or unenchanted piece of [jewelry](/wiki/Skyrim:Jewelry "Skyrim:Jewelry") ([circlet](/wiki/Skyrim:Circlet "Skyrim:Circlet"), [necklace](/wiki/Skyrim:Necklace "Skyrim:Necklace"), or [ring](/wiki/Skyrim:Ring "Skyrim:Ring")); see [Leveled Lists](/wiki/Skyrim:Leveled_Lists#Thieves_Guild_Lists "Skyrim:Leveled Lists") for details. When the quest is started, the item is placed in the inventory of a randomly-selected NPC. Nearly anyone in any of the five main cities can be a target. Notable exceptions include [guards](/wiki/Skyrim:Guards "Skyrim:Guards"), [Thieves Guild](/wiki/Skyrim:Thieves_Guild_(faction) "Skyrim:Thieves Guild (faction)") members, and [children](/wiki/Skyrim:Child "Skyrim:Child"). If [Dragonborn](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") is installed, NPCs in [Raven Rock](/wiki/Skyrim:Raven_Rock "Skyrim:Raven Rock") can also be targets.

You must not be caught and sent to jail while the quest is active, for any reason, otherwise you will fail the quest; you also cannot kill the target. Once you have retrieved the item, return to Delvin for a leveled gold reward.

### Reward

| Levels | Reward |
| --- | --- |
| 1-5 | 50 |
| 6-10 | 100 |
| 11-15 | 150 |
| 16-20 | 200 |
| 21-26 | 250 |
| 27-31 | 300 |
| 32-36 | 350 |
| 37-41 | 400 |
| 42+ | 500 |

## Notes

- If the target is a possible follower, then it is possible to complete this quest without committing a crime; simply recruit the follower and remove the item from their inventory.
- Version 1.3.2 of the [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch") limits the target cities to those found in the base game.
- When giving you this job, one of Delvin's possible lines is *"Got ourselves a freelancer thinks he can muscle in on our territory. How about you teach him some manners, eh?"* This line can still trigger even if the target is female.
- If you get arrested in a hold which is different from the target's hold, the quest still fails. Getting arrested on Solstheim can fail this quest when the target is located on Skyrim.

## Bugs

- The cleanup script will take any similar item rather than the quest item. This cleanup script is run whether you are successful or canceling the job and will remove items from your inventory. Any items that are taken are permanently destroyed so it is recommended that you save and drop all items of the same type (if he wants a gold diamond necklace drop all gold diamond necklaces including custom enchanted ones). You can also work around this bug by giving all items of the same type to a follower.
- After a quest has been completed by returning the pickpocketed item to the quest giver and receiving payment, the item may remain in your inventory, shown as stolen. It may then be sold again to a fence. **?**
- There is a chance that this quest may involve stealing items from a number of people where the chance of the steal will always be 0%, no matter what Pickpocket perks or skill you have.
  - You may request to cancel the quest if this happens.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") Open the console, and click the victim to select them. Type "showinventory" (to find the ID of the quest target). Type "drop <ID number of the quest object> 1". Steal the quest target after it falls to the ground.
  - If you have the *poisoned* perk, you can reverse pickpocket a [paralysis](/wiki/Skyrim:Paralyze_(effect) "Skyrim:Paralyze (effect)") poison into the target. As the potion is coming close to wearing off, there will be a brief moment where you can pickpocket anything with 100% success, and won't get a bounty even if you're seen doing it (because the game *thinks* you're just corpse-looting, which always succeeds and is perfectly legal). However, you have to time your pickpocketing correctly for this to work, so you may want to save before attempting.
- With Dragonborn installed: If you are asked to steal something from one of the crew of the Northern Maiden (the boat that runs between Windhelm and Solstheim), there is a possibility that the item will only be placed in that person's inventory at one end of the journey, and not the other. For example, thanks to there being significantly fewer people around at the Raven Rock end of the journey, it's much easier to pickpocket them there, but no use if the item's only in their pocket when you meet them at the much more highly populated Windhelm dock. **?**
- [Dryston](/wiki/Skyrim:Dryston "Skyrim:Dryston") can be a quest target before he actually appears in the game. If so, the quest marker will point to an empty area of Weylin's room. **?**
  - Either request a new job or advance [The Forsworn Conspiracy](/wiki/Skyrim:The_Forsworn_Conspiracy "Skyrim:The Forsworn Conspiracy") until Dryston appears.

## Quest Stages

| The Fishing Job (TGRGF) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 10 |  | I've been told to pickpocket <Alias=ItemToGet> from <Alias=Mark> in <Alias=City>. I need to complete this job without killing the mark or getting caught and spending time in jail. *Objective 10:* Retrieve <Alias=ItemToGet> from <Alias=Mark> in <Alias=City> |
| 50 |  | I've retrieved <Alias=ItemToGet> from <Alias=Mark> in <Alias=City>. *Objective 20:* Return the <Alias=ItemToGet> to Delvin |
| 200 | ☑ | I've successfully completed the job and received my share of the pay. |
| 250 | ☒ | By killing a resident at the task's location, I've failed this job and was forced to forfeit my share of the pay. |
| ☒ | During the course of this task, I was arrested and sent to the local jail. I've therefore failed the job and was forced to forfeit my share of the pay. |
| ☒ | Before the task could be completed, I decided to quit. I've therefore failed the job and forfeited any pay I might have received. |

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage TGRGF stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest TGRGF`.
