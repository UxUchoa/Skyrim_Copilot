---
source_url: "https://en.uesp.net/wiki/Skyrim:Protected_NPCs"
title: "Skyrim:Protected NPCs"
entity_type: "npc"
namespace: "Skyrim"
retrieved_at: "2026-05-05T00:10:55.909138+00:00"
tags: ["Skyrim-Bugs Fixed by the Official Skyrim Patch", "Skyrim-Confirmed Bugs", "Skyrim-NPCs"]
---

# Skyrim:Protected NPCs

## Overview

Certain NPCs in Skyrim are **protected** at some point during gameplay. This means that when their health depletes (usually down to 10% of its maximum, but this will occur even if the NPC's health would have been reduced to zero), they enter a state called "bleedout", where they fall to their knees and are ignored by all hostile entities until their health regenerates. Unlike the similar [essential](/wiki/Skyrim:Essential_NPCs "Skyrim:Essential NPCs") status, they can still be killed if they are attacked by the player, where they will die as easily as non-protected NPCs.

A permanent [follower](/wiki/Skyrim:Followers "Skyrim:Followers") accompanying the player is set as protected, regardless of whether or not they are normally. This also applies to the player's [spouse](/wiki/Skyrim:Marriage "Skyrim:Marriage") and anyone [recruited](/wiki/Skyrim:Rebuilding_the_Blades "Skyrim:Rebuilding the Blades") into the [Blades](/wiki/Skyrim:Blades "Skyrim:Blades").

To be killed, a protected NPC must have their health fall to zero from a direct hit by the player. An important keyword in this definition is "direct." This can sometimes lead to your follower or spouse surviving attacks from you when you don't expect them to. Namely:

- Fall damage from the [Unrelenting Force](/wiki/Skyrim:Unrelenting_Force "Skyrim:Unrelenting Force") shout will not kill a protected NPC.
- A poison slipped into your spouse's or inactive follower's pocket (Note: Only inactive followers can be pickpocketed) using the [Poisoned skill perk](/wiki/Skyrim:Poisoned "Skyrim:Poisoned") will only bring the Protected NPC into bleedout, even if that same poison would kill the protected NPC if it were applied to the player's weapon.

For a list of protected NPCs, see [Category:Skyrim-Protected NPCs](/wiki/Category:Skyrim-Protected_NPCs "Category:Skyrim-Protected NPCs") and for a list of protected creatures, see [Category:Skyrim-Protected Creatures](/wiki/Category:Skyrim-Protected_Creatures "Category:Skyrim-Protected Creatures").

## Notes

- Hostiles (like [Draugr](/wiki/Skyrim:Draugr "Skyrim:Draugr") and [bandits](/wiki/Skyrim:Bandit "Skyrim:Bandit")) have a state similar to being "protected", but it does not offer the same benefit: when they enter the bleedout state, their attackers will ignore them and instead concentrate on any other hostiles in the area (such as other Draugr and bandits) before finally turning their attention back on them, even if they are still in bleedout. If there are no other hostiles in the area, the attackers will concentrate on them until they are destroyed.
- Active Followers can still kill protected NPCs, but conjured creatures cannot.

## Bugs

- A protected NPC may still be killed by other NPCs if they are attacked during bleedout, commonly by area of effect magic, poison or delayed power attacks.
  - The [Official Skyrim Patch](/wiki/Skyrim:Patch "Skyrim:Patch"), version Beta 1.9.26.0.8, fixes this bug.
- Characters brought to the bleedout state may not stand back up, leading to them crawling along the floor.
  - Using [Unrelenting Force](/wiki/Skyrim:Unrelenting_Force "Skyrim:Unrelenting Force"), casting [paralyze](/wiki/Skyrim:Paralyze_(spell) "Skyrim:Paralyze (spell)") or sprinting into them may reset their animation.
- Sometimes, after entering the bleedout state and standing back up, NPCs may not have regenerated their health: rather, it remains at the percentage when they fell to their knees originally. This might happen two or more times in a row before they finally regain full health.
