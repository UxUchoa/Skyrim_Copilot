---
source_url: "https://en.uesp.net/wiki/Skyrim:Lisbet's_Missing_Shipment"
title: "Skyrim:Lisbet's Missing Shipment"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:41:38.046562+00:00"
tags: ["Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Confirmed Bugs", "Skyrim-Quests", "Skyrim-Quests which affect Disposition", "Skyrim-Quests-Miscellaneous-Favors", "Skyrim-Quests-Miscellaneous-Radiant", "Skyrim-Quests-Radiant", "Skyrim-SRQRP-Requires Final Review"]
---

# Skyrim:Lisbet's Missing Shipment

## Overview

|  |  |
| --- | --- |
| **Retrieve a missing Dibella Statue for a struggling store.** | |

|  |  |
| --- | --- |
| Quest Giver: | [Lisbet](/wiki/Skyrim:Lisbet "Skyrim:Lisbet") |
| Location(s): | [Arnleif and Sons Trading Company](/wiki/Skyrim:Arnleif_and_Sons_Trading_Company "Skyrim:Arnleif and Sons Trading Company") |
| Reward: | Leveled [Gold](/wiki/Skyrim:Gold "Skyrim:Gold") |
| [Disposition](/wiki/Skyrim:Disposition "Skyrim:Disposition"): | =2 ([Lisbet](/wiki/Skyrim:Lisbet "Skyrim:Lisbet")) |
| ID: | FreeformMarkarthE |
| Difficulty: | Medium |

[![](//images.uesp.net/thumb/0/06/SR-quest-Lisbet%27s_Missing_Shipment.jpg/200px-SR-quest-Lisbet%27s_Missing_Shipment.jpg)](/wiki/File:SR-quest-Lisbet%27s_Missing_Shipment.jpg)

*"You aren't for hire, are you?"*

## Quick Walkthrough

1. Speak to [Lisbet](/wiki/Skyrim:Lisbet "Skyrim:Lisbet").
2. Retrieve [Lisbet's Dibella Statue](/wiki/Skyrim:Lisbet%27s_Dibella_Statue "Skyrim:Lisbet's Dibella Statue").
3. Return to Lisbet.

### An Empty Store

Near the market in [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth") is the general goods store, [Arnleif and Sons Trading Company](/wiki/Skyrim:Arnleif_and_Sons_Trading_Company "Skyrim:Arnleif and Sons Trading Company"), where the proprietor [Lisbet](/wiki/Skyrim:Lisbet "Skyrim:Lisbet") is struggling to keep her business afloat. Not only did she lose her husband, Gunnar, in a [Forsworn](/wiki/Skyrim:Forsworn "Skyrim:Forsworn") attack, she also lost dozens of shipments to the Forsworn, including a precious, specially-made Statue of Dibella. She believes this statue would put the store back on its feet. When you speak with her, she is ashamed of the state of her shop and will then ask you a question: *"You aren't for hire, are you? A sellsword? I'll pay you if you can recover that statuette from the Forsworn."* Accept the task and she will promise you a great sum of gold for your efforts and the quest will be added to your journal.

### The Statue of Dibella

Once you have accepted Lisbet's request, your map marker will point you towards one of eight possible Forsworn hideouts, where you will find the [Lisbet's Dibella Statue](/wiki/Skyrim:Lisbet%27s_Dibella_Statue "Skyrim:Lisbet's Dibella Statue") in the location's boss chest:

| Possible Locations |
| --- |
| [Broken Tower Redoubt](/wiki/Skyrim:Broken_Tower_Redoubt "Skyrim:Broken Tower Redoubt"), [Bruca's Leap Redoubt](/wiki/Skyrim:Bruca%27s_Leap_Redoubt "Skyrim:Bruca's Leap Redoubt"), [Deepwood Redoubt](/wiki/Skyrim:Deepwood_Redoubt "Skyrim:Deepwood Redoubt"), [Dragon Bridge Overlook](/wiki/Skyrim:Dragon_Bridge_Overlook "Skyrim:Dragon Bridge Overlook"), [Druadach Redoubt](/wiki/Skyrim:Druadach_Redoubt "Skyrim:Druadach Redoubt"), [Hag Rock Redoubt](/wiki/Skyrim:Hag_Rock_Redoubt "Skyrim:Hag Rock Redoubt"), [Red Eagle Redoubt](/wiki/Skyrim:Red_Eagle_Redoubt "Skyrim:Red Eagle Redoubt"), [Serpent's Bluff Redoubt](/wiki/Skyrim:Serpent%27s_Bluff_Redoubt "Skyrim:Serpent's Bluff Redoubt") |

Once you have claimed the statue, return to Lisbet in her store. When presented with the item, she is overjoyed, saying: *"Ah, there it is! This little gold delight is going to keep us afloat for a while. Thank you. Here's something for your hard work."* She will then hand you a leveled amount of gold as a reward.

### Reward

|  |
| --- |
| | Levels | Reward | | --- | --- | | 1–9 | 500 | | 10–19 | 750 | | 20–29 | 1,000 | | 30–39 | 1,250 | | 40+ | 1,500 | |

## Notes

- Oddly, you may be able to buy the statue back from her for *less* than your reward at any level.

## Bugs

- If you retrieve the statue after the completion of this quest, it will become stuck in your inventory as a quest item.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.5, fixes this bug.
- You are prevented from starting this quest if you've already killed all enemies in the Forsworn camp before talking to Lisbet.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") Enter `setstage FreeformMarkarthE 12` to skip forward in the quest.
- In case Lisbet is killed before completing the quest, both statue and objective will get stuck.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") Enter `setstage FreeformMarkarthE 20` to manually complete the quest: you will receive the reward, and the statue will be removed from your inventory.

## Quest Stages

| Lisbet's Missing Shipment (FreeformMarkarthE) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 10 |  | *Objective 10:* Retrieve Lisbet's shipment from <Alias=ForswornCamp> |
| 15 |  | *Objective 15:* Bring the Dibella Statue to Lisbet |

- The following empty quest stages were omitted from the table: 12, 20.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage FreeformMarkarthE stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest FreeformMarkarthE`.
