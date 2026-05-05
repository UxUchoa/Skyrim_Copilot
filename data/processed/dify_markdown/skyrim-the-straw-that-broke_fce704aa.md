---
source_url: "https://en.uesp.net/wiki/Skyrim:The_Straw_that_Broke"
title: "Skyrim:The Straw that Broke"
entity_type: "quest"
namespace: "Skyrim"
retrieved_at: "2026-05-04T23:46:30.381991+00:00"
tags: ["Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Confirmed Bugs", "Skyrim-Quests", "Skyrim-Quests which affect Disposition", "Skyrim-Quests-Miscellaneous-Favors", "Skyrim-SRQRP-Requires Final Review", "Skyrim-Unconfirmed Bugs"]
---

# Skyrim:The Straw that Broke

## Overview

|  |  |
| --- | --- |
| **Discover what is plaguing [Narfi](/wiki/Skyrim:Narfi "Skyrim:Narfi")'s mind.** | |

|  |  |
| --- | --- |
| Quest Giver: | [Narfi](/wiki/Skyrim:Narfi "Skyrim:Narfi") |
| Location(s): | [Ivarstead](/wiki/Skyrim:Ivarstead "Skyrim:Ivarstead") |
| Reward: | Random rare [Ingredients](/wiki/Skyrim:Ingredients "Skyrim:Ingredients") |
| [Disposition](/wiki/Skyrim:Disposition "Skyrim:Disposition"): | =1 ([Narfi](/wiki/Skyrim:Narfi "Skyrim:Narfi")) |
| ID: | FreeformIvarstead02 |

[![](//images.uesp.net/thumb/5/5c/SR-quest-The_Straw_that_Broke.jpg/200px-SR-quest-The_Straw_that_Broke.jpg)](/wiki/File:SR-quest-The_Straw_that_Broke.jpg)

*"You live among the clouds now, dear Reyda!"*

## Quick Walkthrough

1. Discover what is plaguing [Narfi](/wiki/Skyrim:Narfi "Skyrim:Narfi")'s mind.
2. Find [Reyda's Necklace](/wiki/Skyrim:Reyda%27s_Necklace "Skyrim:Reyda's Necklace").
3. Return the necklace to Narfi.

### Grief

When you visit [Narfi](/wiki/Skyrim:Narfi "Skyrim:Narfi") in [Ivarstead](/wiki/Skyrim:Ivarstead "Skyrim:Ivarstead"), you will quickly find that all is not well with him. Narfi lives in his parents' broken-down house across the river from the lumber mill. When speaking to him, you will notice that he has a mental disability and is very distraught over the disappearance of his sister, Reyda. He will mention that [Wilhelm](/wiki/Skyrim:Wilhelm "Skyrim:Wilhelm"), the innkeeper at [Vilemyr Inn](/wiki/Skyrim:Vilemyr_Inn "Skyrim:Vilemyr Inn"), told him Reyda would come back, and that he needs to say goodbye to his sister like he did his mother and father.

### Pity

When speaking to Wilhelm, he will tell you that Narfi is harmless, but in a state since his sister disappeared. Wilhelm, meaning well, told Narfi his sister would return one day, but actually fears Reyda was killed while searching for [ingredients](/wiki/Skyrim:Ingredients "Skyrim:Ingredients") from the river. He will point you in the direction of the small island to the east of Ivarstead, where you can then go look for Narfi's sister. There is a small barrow dungeon on that island, [Geirmund's Hall](/wiki/Skyrim:Geirmund%27s_Hall "Skyrim:Geirmund's Hall"), and it seems like the obvious place to start.

### Truth

Though Wilhelm's supposition about Reyda's fate turns out to be correct his directions are inaccurate. Reyda's remains are not at the island, but can be found underwater just east of the southern bridge into town. Due to the current they may be difficult to access. Next to her remains are [her necklace](/wiki/Skyrim:Reyda%27s_Necklace "Skyrim:Reyda's Necklace") and a [satchel](/wiki/Skyrim:Satchel "Skyrim:Satchel"); the satchel contains some gold and several random alchemical ingredients. Return the necklace to Narfi. You can tell him the truth about what happened to Reyda, or assure him she will come back. In either case, you will receive three random, rare ingredients, and Narfi will, for the most part, remain the same.

## Notes

- Narfi is the victim of the Dark Brotherhood quest [Kill Narfi](/wiki/Skyrim:Kill_Narfi "Skyrim:Kill Narfi"). Once you accept the assassin quest, it will be impossible to complete the Reyda quest successfully.
  - To complete both the Dark Brotherhood quest and the miscellaneous quest after accepting the contract from Nazir, you can use the console command "setstage DBsidecontract01 20" to be able to speak to Narfi about his sister. This will mark that you have killed Narfi while he is still alive, but you can simply kill him after completing his side quest to set you back on track, or use the console command "setstage DBsidecontract01 10" to set you back to the step where you have access to the relevant dialogue and must kill Narfi to continue.

## Bugs

- If you show Reyda's necklace to Wilhelm, his reaction is exactly the same as Narfi's: *"Reyda! You saw Reyda? Did you tell her Narfi cries? Did you tell her Narfi never said goodbye like mother and father?"*
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.5, fixes this bug.
  - Special Edition seems to have patched this. The dialogue option is no longer present. This might only apply to Xbox.
- If you take the necklace from Reyda's satchel before asking Wilhelm about Narfi, the quest will not update beyond the stage requiring you to find her remains even if you search the satchel again.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.3.2, fixes this bug.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://www.wikipedia.org/wiki/PC_game "PC") The command `setstage FreeformIvarstead02 40` will do the work.
  - Dropping and retaking the necklace using the console command `player.drop 663da 1` while standing over the underwater satchel causes a quest update, fixing the quest.
- Narfi may quit dialogue without giving you a chance to tell him about Reyda's fate and finish the quest.
- Going straight to Reyda's corpse after accepting the quest instead of talking to Wilhelm will leave the log entry about asking Wilhelm in your miscellaneous quests tab even after the quest, and Wilhelm will have no topic about Reyda should you visit later. The only way to fix this is by returning the quest to an earlier stage by using the command `setstage FreeformIvarstead02 20` and redoing the quest in proper sequence.
- [![Flag Germany.png](//images.uesp.net/thumb/9/90/Flag_Germany.png/22px-Flag_Germany.png)](/wiki/File:Flag_Germany.png) Reyda's name is frequently misspelled as Rayda in the German translations of Narfi's dialogue. **?**
- Completing this quest would make Narfi unavailable to become a [farmhand](/wiki/Skyrim:Farmhand "Skyrim:Farmhand")[CC](/wiki/Skyrim:Farming "Skyrim:Farming").
  - Recruiting him to be a farmhand first is a workaround.

## Quest Stages

| The Straw that Broke (FreeformIvarstead02) | | |
| --- | --- | --- |
| Stage | Finishes Quest | Journal Entry |
| 20 |  | *Objective 10:* Ask Wilhelm about Reyda |
| 30 |  | *Objective 20:* Locate Reyda's remains |
| 40 |  | *Objective 30:* Bring Reyda's Necklace to Narfi |
| 200 | ☑ |  |

- The following empty quest stages were omitted from the table: 10, 250.

Notes

- Any text displayed in angle brackets (e.g., `<Alias=LocationHold>`) is dynamically set by the Radiant Quest system, and will be filled in with the appropriate word(s) when seen in game.
- Not all Journal Entries may appear in your journal; which entries appear and which entries do not depends on the manner in which the quest is done.
- Stages are not always in order of progress. This is usually the case with quests that have multiple possible outcomes or quests where certain tasks may be done in any order. Some stages may therefore repeat objectives seen in other stages.
- If an entry is marked as "Finishes Quest" it means the quest disappears from the Active Quest list, but you may still receive new entries for that quest.
- On the PC, it is possible to use the [console](/wiki/Skyrim:Console "Skyrim:Console") to advance through the quest by entering `setstage FreeformIvarstead02 stage`, where `stage` is the number of the stage you wish to complete. It is not possible to un-complete (i.e. go back) quest stages, but it is possible to clear all stages of the quest using `resetquest FreeformIvarstead02`.
