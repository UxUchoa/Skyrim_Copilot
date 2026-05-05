---
source_url: "https://en.uesp.net/wiki/Skyrim:If_I_had_a_Hammer"
title: "Skyrim:If I had a Hammer"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:40:31.095985+00:00"
tags: ["MetaTemplate-Load", "Skyrim-Creation Club-Quests", "Skyrim-Quests", "Skyrim-SRQRP-Requires Final Review", "Skyrim-Stendarr's Hammer", "Skyrim-Unconfirmed Bugs"]
---

# Skyrim:If I had a Hammer

## Overview

|  |  |
| --- | --- |
| [SR-qico-Miscellaneous.png](/wiki/File:SR-qico-Miscellaneous.png) | **Steal a legendary hammer of the gods.** |

|  |  |
| --- | --- |
| Quest Giver: | Automatically added after purchasing the [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer "Skyrim:Stendarr's Hammer") [Creation](/wiki/Skyrim:Creation_Club "Skyrim:Creation Club") (not visible in journal) |
| Location(s): | [Understone Keep](/wiki/Skyrim:Understone_Keep "Skyrim:Understone Keep") |
| Reward: | [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer_(item) "Skyrim:Stendarr's Hammer (item)") |
| ID: | ccBGSSSE006\_Quest |
| Added by: | [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer "Skyrim:Stendarr's Hammer") |

[![](//images.uesp.net/thumb/7/75/SR-quest-If_I_had_a_Hammer.jpg/200px-SR-quest-If_I_had_a_Hammer.jpg)](/wiki/File:SR-quest-If_I_had_a_Hammer.jpg)

Stendarr's Hammer in the Dwemer Museum

## Quick Walkthrough

**Note**: This quest does not appear in your journal.

1. Gain entry to the [Dwemer Museum](/wiki/Skyrim:Dwemer_Museum "Skyrim:Dwemer Museum") in [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth").
2. Take [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer_(item) "Skyrim:Stendarr's Hammer (item)").

## Detailed Walkthrough

**Note: This quest was originally added to your journal upon installing the [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer "Skyrim:Stendarr's Hammer") [Creation](/wiki/Skyrim:Creation_Club "Skyrim:Creation Club"). With the release of the [Anniversary Edition](/wiki/Skyrim:Anniversary_Edition "Skyrim:Anniversary Edition"), this quest no longer appears in your journal. Stendarr's Hammer can still be acquired from the Dwemer Museum.**

Go to the [Dwemer Museum](/wiki/Skyrim:Dwemer_Museum "Skyrim:Dwemer Museum") in [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth") to steal [Stendarr's Hammer](/wiki/Skyrim:Stendarr%27s_Hammer_(item) "Skyrim:Stendarr's Hammer (item)").

Note that without a [key](/wiki/Skyrim:Dwemer_Museum_Key "Skyrim:Dwemer Museum Key") and [Calcelmo](/wiki/Skyrim:Calcelmo "Skyrim:Calcelmo")'s permission, entry to the Museum is considered trespassing, and the guards inside will attempt to arrest you. In order to gain access to the museum, see the quest [Hard Answers](/wiki/Skyrim:Hard_Answers "Skyrim:Hard Answers") for more information on gaining entrance. Alternatively, you can simply pick the lock and sneak past the guards.

Picking up Stendarr's Hammer does not count as theft. However, it is exceedingly heavy (100 weight), so keep this in mind to avoid getting over-encumbered.

## Notes

- Prior to the Anniversary Edition update, you would receive this quest upon installing the Stendarr's Hammer Creation (or upon exiting [Helgen](/wiki/Skyrim:Helgen "Skyrim:Helgen") on a new character). With Anniversary Edition installed, there is now no notification or quest for this Creation.

## Bugs

- The quest can remain incomplete after your successful theft of the Hammer. `sqs ccBGSSSE006_Quest`  will show stage 1000 as a 0. Use `completequest ccBGSSSE006_Quest`  to get around this. **?**

## Quest Stages

| If I had a Hammer (ccBGSSSE006\_Quest) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 100 |  | Rumor has it that Stendarr's Hammer has been found deep under Markarth. They say it is in the Dwarven Museum there. *Objective :* Steal Stendarr's Hammer |
| 1000 | ☑ | I have successfully stolen Stendarr's Hammer from the Dwarven Museum in Markarth. |

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage ccBGSSSE006_Quest stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest ccBGSSSE006_Quest`.
