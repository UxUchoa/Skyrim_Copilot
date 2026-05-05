---
source_url: "https://en.uesp.net/wiki/Skyrim:Classes"
title: "Skyrim:Classes"
entity_type: "npc"
namespace: "Skyrim"
retrieved_at: "2026-05-05T00:17:39.787536+00:00"
tags: ["Category", "Skyrim-NPCs"]
---

# Skyrim:Classes

## Overview

In Skyrim, a **class** cannot be chosen by the player character, but is instead used by [NPCs](/wiki/Skyrim:NPCs "Skyrim:NPCs"). There may be some classes that appear identical to each other. The difference between such classes are the [services](/wiki/Skyrim:Services "Skyrim:Services") offered, which are not listed here.

## Skill and Attribute Weights

The numbers in the table are the weights assigned by the classes to each [skill](/wiki/Skyrim:Skills "Skyrim:Skills") and each [attribute](/wiki/Skyrim:Attributes "Skyrim:Attributes") (empty cells have a weight of zero). These weights determine how many of 8 skill points and 10 attribute points per level are added to each value. Note that 5 points per gained level are always added to [Health](/wiki/Skyrim:Health "Skyrim:Health"), *in addition to* any health points from the shared set of 10 attribute points; this means NPCs gain 15 attributes per level, in addition to *approximately* 8 skill points per level (see below).

Unlike the PC, there is no intrinsic mechanism for an NPC to gain *perks* as they level; a stock leveled NPC has the same perks at any level. This is one of the reasons [leveled lists](/wiki/Skyrim:Leveled_Lists "Skyrim:Leveled Lists") exist. For example, a [Bandit](/wiki/Skyrim:Bandit "Skyrim:Bandit") Thug and a Bandit Highwayman are fundamentally the same NPC at levels 9 and 14, respectively (they are both members of the Bandit Archer class, below), but the former has the [Extra Damage 1.5](/wiki/Skyrim:Extra_Damage_1.5 "Skyrim:Extra Damage 1.5") perk, while the latter has [Extra Damage 2](/wiki/Skyrim:Extra_Damage_2 "Skyrim:Extra Damage 2"). Because perks are manually assigned to an NPC independently of its level or class (and hence independently of its skill expertise and attributes), mismatches exist; this is particularly noticeable among [followers](/wiki/Skyrim:Followers "Skyrim:Followers").

Class and perks are also not automatically tied to equipment or spells in any way, leading to the same mismatches; while the aforementioned Thug and Highwayman share the same leveled lists for equipment, and their level is used to determine what they have, these lists were assigned manually, not by the class (or [race](/wiki/Skyrim:Races "Skyrim:Races")). Typically, these mismatches are less obviously unintentional, particularly when an NPC lacks *any* equipment, but still sometimes leads to followers carrying weapons they do not know how to use.

### Attribute Weights

The game ensures attribute points are not lost or gained due to rounding, but it is easy for an NPC's number of attribute points to not be an integer multiple of a weight (for example, Imperial Soldiers have a Stamina weight of 7, but can be level 37). Attribute points are actually assigned as follows:

1. Calculate the total number of points available (10 \* (level - 1))
2. Calculate the result for the attribute with the highest weight, rounded down, and subtract that from the total.
   - In the event of a tie, choose Health over Magicka or Stamina, and Magicka over Stamina.
3. Repeat for the next-highest result, remembering to use the ratio of only the two remaining attributes.
4. Any remaining points go to the last attribute.

This means there is a weighting bias in favor of Stamina over Magicka and Magicka over Health, because Stamina is intrinsically chosen last and gets anything the others lost due to rounding, but Health gets 1/3 of each level's attribute points before assignment. For example:

- A beggar has weights 1, 1, 1 - all equal. A beggar at level 8 (70 attribute points, plus 35 mandatory health points) calculates as follows:
  1. Health is assigned 23 points (70/3, rounded down), then adds 35: Health +58.
  2. Magicka is assigned 23 points ((70-23)/2, rounded down): Magicka +23.
  3. Stamina is assigned 24 points (70-23-23): Stamina +24.

### Skill Weights

In the "Primary Skills" summary on individual NPC pages, skills with values of 3 or greater are normally emphasized in **bold** face, skills with a value of 2 are shown in normal font, and skills with a value of 1 or 0 are not listed. However, on NPCs with a fixed low level, the displayed skills are adjusted taking into account racial skill bonuses, with only skills greater than 25 being shown.

Unlike with Attributes, an NPC is capable of "losing" or "gaining" skill points due to rounding; a skill gains skill points in accordance with:

```
This Skill Points = round(Total Skill Points * (This Skill Weight / Sum of Skill Weights))
```

Where Total Skill Points = (Level-1)\*8; an NPC's skill points at level 1 are 15 (a game-wide constant) base, then modified by its race.

Note the *drastic* difference between NPCs and the PC: for the PC, each [level](/wiki/Skyrim:Leveling "Skyrim:Leveling") takes more skill ranks than the level before did, while NPCs gain a linear (aside from rounding errors) number of skill points per level. On the other hand, the PC needs less than 8 skill points to level initially (only 4 are needed in the skill the PC's race is best at to level) and that number depends on which skill is being leveled (since the 100th rank in a skill counts for more than the 16th); assuming the PC is leveling as quickly as possible, their skill ranks per level will only *exceed* 8 (meaning the NPCs have begun "winning") at level 33.

Because NPCs face the same skill maximum of 100 ranks as the PC, however, and unlike the PC, will *not* resort to putting skill points into non-preferential (0 weight, below) skills - the formula above *always* holds true - past a certain point, which depends on the NPC's class, they will cease to gain *any* skill points per level, and will only gain attributes. An excellent example of this is [Arngeir](/wiki/Skyrim:Arngeir "Skyrim:Arngeir"), who is level 150, but stopped gaining skill points at level 139 (which is when he reached 100 ranks in Enchanting). In addition, none of his leveled skills *do* anything - he has no weapons or armor to smith or enchant (nor would he, if he did have them - NPCs with crafting skills do not automatically craft anything), no potions indicative of his alchemy, no spells to cast with conjuration or restoration (he only has shouts), and no way to use the speech skill. This is indicative of how the game usually works - there is simply no framework in place allowing NPCs to "automatically" employ their skills, so it has to be assigned manually. This is why you routinely see NPCs like Arngeir, with magic skills but no spells to cast with them, crafting skills but nothing crafted to show for it (which is why the PC is the only source of smithed gear in the game - NPCs *never* carry Fine or better gear), speech without relatively increased money or gear quality (as is found on the PC), etc.

#### Mismatch Examples

As the table below shows, many physical-combat-oriented classes such as [Stormcloak](/wiki/Skyrim:Stormcloaks "Skyrim:Stormcloaks") ("Sons of Skyrim") Guards and Soldiers (Class IDs `GuardSonsSkyrim` and `SoldierSonsSkyrimNotGuard` respectively) and [Orc](/wiki/Skyrim:Orc "Skyrim:Orc") Warriors (`GuardOrc1H` and `GuardOrc2H`) have no magic skills, yet are weighted toward [Magicka](/wiki/Skyrim:Magicka "Skyrim:Magicka") as well as [Health](/wiki/Skyrim:Health "Skyrim:Health") as their levels increase, leaving them with stunted [Stamina](/wiki/Skyrim:Stamina "Skyrim:Stamina"). Consequently, if you keep them in melee range but avoid or [Block](/wiki/Skyrim:Block "Skyrim:Block") (or simply withstand) their swings, they rapidly become less dangerous than they should be, from exhaustion. They are also an unexpectedly good source of unused Magicka to [Absorb](/wiki/Skyrim:Absorb_Magicka "Skyrim:Absorb Magicka") from them during the fight.

Numerous NPCs likewise come with gear that is not suited at all to their specializations (e.g. [Light Armor](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") when they should have [Heavy](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor"), or [One-handed](/wiki/Skyrim:One-handed "Skyrim:One-handed") weapons when they should have [Two-handed](/wiki/Skyrim:Two-handed "Skyrim:Two-handed")). If gear they should prefer is dropped near them, they will not pick it up and switch. Even using the [Console](/wiki/Skyrim:Console "Skyrim:Console") to give them armor they should like will not make them auto-equip any of it in most cases, due to the game's pre-set Outfits system; they typically must be forced to equip it with `EquipItem <BaseID>`. (This does not apply to long-term followers, who provide inventory access, though you sometimes have to take things away from them to get them to use what you want.)

A more specific example of how the lack of automatic perks and gear can lead to apparent absurdity is provided by the three [Dawnguard](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") followers that have no maximum level: [Celann](/wiki/Skyrim:Celann "Skyrim:Celann"), [Durak](/wiki/Skyrim:Durak "Skyrim:Durak"), and [Ingjard](/wiki/Skyrim:Ingjard "Skyrim:Ingjard"), particularly without the [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch").

Ingjard has no perks at all, but is a [Nord](/wiki/Skyrim:Nord "Skyrim:Nord") `CombatWarrior2H`, meaning she reaches 100 skill in Two-handed very quickly (at level 36), then stops getting any better at it. [Celann](/wiki/Skyrim:Celann "Skyrim:Celann") is a [Breton](/wiki/Skyrim:Breton "Skyrim:Breton") `CombatWarrior1H`, meaning he reaches 100 in the same skill *much* slower (level 118), but he has the [Extra Damage 1.5](/wiki/Skyrim:Extra_Damage_1.5 "Skyrim:Extra Damage 1.5") perk, meaning he will do the same damage as Ingjard once he reaches skill 80 at level 90, and then continue on to surpass her; in addition, he inexplicably has [Champion's Stance](/wiki/Skyrim:Champion%27s_Stance "Skyrim:Champion's Stance"), letting him power attack more often than she does right from the start, with the same Two-handed weapons he does not have any skill with yet.

Meanwhile, both Celann and Durak have [Custom Fit](/wiki/Skyrim:Custom_Fit "Skyrim:Custom Fit"), even though Celann has *zero* skill weight on Light Armor (Durak does have skill weight on Light Armor); *both* wear Light Armor stock, so Durak will be drastically more durable if you do not issue Celann new gear, and even if you do give him some heavy armor, he will be at a constant disadvantage.

None of the three has access to any sort of leveled lists for gear, so they will carry the same gear at any level unless you give them something better to carry.

## List of Classes

| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [Combat](/wiki/Skyrim:Combat "Skyrim:Combat") | | | | | |  | [Magic](/wiki/Skyrim:Magic "Skyrim:Magic") | | | | | |  | [Stealth](/wiki/Skyrim:Stealth "Skyrim:Stealth") | | | | | |  | [Attributes](/wiki/Skyrim:Attributes "Skyrim:Attributes") | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Alik'r Archer | EncClassAlikrMissile | 0006766c | 3 | 1 | 1 | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 3 |  | 2 |
| Alik'r Warrior | EncClassAlikrMelee | 0006766b |  | 2 | 1 | 3 |  | 3 |  |  |  |  |  |  |  |  |  | 2 |  |  |  |  |  | 3 |  | 2 |
| Alik'r Wizard | EncClassAlikrWizard | 0006766d |  |  |  |  |  |  |  |  | 2 | 3 |  | 2 | 2 |  |  | 1 |  |  | 1 |  |  | 2 | 3 |  |
| Apothecary | TrainerAlchemyExpert | 000e3a6e |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  | 4 |  |  | 2 | 2 | 3 |  | 1 | 1 | 1 |
| Apothecary | TrainerAlchemyJourneyman | 000e3a5d |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  | 3 |  |  | 2 | 2 | 3 |  | 1 | 1 | 1 |
| Apothecary | VendorApothecary | 00013258 |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  | 3 |  |  | 2 | 2 | 3 |  | 1 | 1 | 1 |
| Ash Guardian[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassAshGuardian | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")03cf6a |  | 1 |  | 2 |  | 1 |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 2 | 2 | 2 |
| Ash Hopper[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassAshHopper | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")020e8a | 3 | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| Assassin | CombatAssassin | 0001317f | 2 |  |  | 3 |  |  |  | 1 |  |  |  |  |  |  |  | 2 |  |  | 3 |  |  | 2 | 1 | 3 |
| Assassin | TrainerAlchemyMaster | 000e3a67 | 4 |  |  | 3 |  |  |  | 1 |  |  |  |  |  |  |  | 2 |  |  | 3 |  |  | 2 | 1 | 3 |
| Assassin | TrainerLightArmorMaster | 000e3a68 | 2 |  |  | 3 |  |  |  | 1 |  |  |  |  |  |  |  | 4 |  |  | 3 |  |  | 2 | 1 | 3 |
| Atronach | EncClassAtronachFlame | 000ad235 | 2 | 1 |  | 3 |  |  |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 2 | 3 | 1 |
| Atronach | EncClassAtronachFrost | 000ad236 | 1 | 3 |  | 2 |  |  |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 3 | 1 | 2 |
| Atronach | EncClassAtronachStorm | 000ad237 |  | 1 |  | 2 |  | 1 |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 2 | 2 | 2 |
| Bandit | EncClassBanditMelee | 0001ce17 |  | 2 | 1 | 3 |  | 3 |  |  |  |  |  |  |  |  |  | 2 |  |  |  |  |  | 3 |  | 2 |
| Bandit[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassBanditBoss | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")01e8ac |  |  | 2 | 3 |  |  |  | 2 |  | 3 |  |  | 1 |  |  |  |  |  | 1 |  |  | 3 | 2 |  |
| Bandit Archer | EncClassBanditMissile | 00015be7 | 3 | 1 | 1 | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 3 |  | 2 |
| Bandit Archer[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassRiekling | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")03bd08 | 3 | 1 |  | 1 |  | 2 |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 3 |  | 2 |
| Bandit Wizard | EncClassBanditWizard | 00039d30 |  |  |  | 1 |  |  |  | 2 |  | 3 |  |  | 2 |  |  | 1 |  |  | 2 |  |  | 2 | 3 |  |
| Barbarian | CombatBarbarian | 0001ce16 | 2 | 2 |  | 1 |  | 3 |  |  |  |  |  |  |  |  |  | 3 |  |  |  |  |  | 4 |  | 2 |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Bard | Bard | 0001325d | 1 |  |  | 1 |  |  |  | 2 |  |  |  | 2 |  |  |  |  |  | 2 |  | 4 |  | 2 | 3 | 2 |
| Bard | TrainerSpeechcraftExpert | 000e3a70 | 1 |  |  | 1 |  |  |  | 2 |  |  |  | 2 |  |  |  |  |  | 2 |  | 4 |  | 2 | 3 | 2 |
| Beggar | Beggar | 0001327b | 1 | 1 |  | 1 | 1 |  |  | 1 |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 2 | 4 |  | 1 | 1 | 1 |
| Blacksmith | TrainerHeavyArmorExpert | 000e3a60 | 2 | 3 |  | 3 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 2 | 2 | 1 |
| Blacksmith | TrainerHeavyArmorMaster | 000e7f45 |  |  |  | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |  | 3 |  | 3 |
| Blacksmith | TrainerLightArmorExpert | 000e3a61 | 2 |  |  | 2 | 3 |  |  |  |  |  |  |  |  |  |  | 3 |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Blacksmith | TrainerLightArmorJourneyman | 000b8340 | 2 |  |  | 2 | 2 |  |  |  |  |  |  |  |  |  |  | 3 |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Blacksmith | TrainerSmithingExpert | 000e3a5f |  |  |  | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Blacksmith | TrainerSmithingJourneyman | 000aedd2 |  |  |  | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Blacksmith | TrainerSmithingMaster | 00042dc1 |  |  |  | 2 | 4 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Blacksmith | VendorBlacksmith | 00013257 |  | 2 |  | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  | 2 | 1 | 2 |
| Blade | Blade | 00021a74 | 3 | 2 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  |  | 3 | 3 |  |
| Chaurus | EncClassChaurus | 00044cca | 3 | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| ChaurusFlyer[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | DLC1\_EncClassChaurusFlyer | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")005206 | 3 | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| Child | Child | 00013279 |  |  |  |  | 4 |  |  |  |  |  | 4 |  |  |  | 4 |  |  | 1 | 2 | 1 |  |  |  | 1 |
| Citizen | Citizen | 0001326b | 2 |  |  | 2 | 3 |  |  |  |  |  | 3 |  |  |  | 3 | 2 |  |  | 2 | 2 |  | 1 | 1 | 1 |
| Conjurer | CombatMageConjurer | 0001ce14 |  |  |  |  |  |  |  | 2 | 3 | 2 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Conjurer | CombatMageNecro | 000c969f |  |  |  | 2 |  |  |  | 2 | 3 |  |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Conjurer | TrainerConjurationExpert | 000e3a78 |  |  |  |  |  |  |  | 2 | 3 | 2 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Conjurer | TrainerConjurationMaster | 000e3a6a |  |  |  |  |  |  |  | 2 | 4 | 2 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Death Hound[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | DLC1EncClassDeathhound | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")0145dc | 2 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  |  | 4 |  | 2 |
| Destruction Mage | CombatMageDestruction | 0001e7d0 |  |  |  |  |  |  |  | 2 | 1 | 3 |  |  | 3 |  |  |  |  |  | 2 |  |  | 2 | 4 |  |
| Destruction Mage | TrainerDestructionExpert | 000e3a5c |  |  |  |  |  |  |  | 2 | 1 | 3 |  |  | 3 |  |  |  |  |  | 2 |  |  | 2 | 4 |  |
| DLC2Ralis | DLC2dunKolbjornRalisClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")0179c6 |  | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 2 |  |  | 2 | 2 | 1 |
| Dragon | EncClassDragon | 0002f201 | 3 | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 |  |  | 4 |  | 2 |
| Dragon Priest | EncClassDragonPriest | 0001ce1c |  |  |  |  |  |  |  | 3 | 5 | 6 |  |  | 5 |  |  |  |  |  |  |  |  | 3 | 3 |  |
| Draugr Melee | EncClassDraugrMelee | 00023c0c |  | 2 | 2 | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  | 3 |
| Draugr Missile | EncClassDraugrMissile | 00023c0d | 3 |  | 2 | 3 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 3 |  | 3 |
| Draugr Warlock | EncClassDraugrMagic | 00023c0e |  |  |  | 2 |  |  |  |  | 3 | 3 |  |  | 2 |  |  |  |  |  | 2 |  |  | 3 | 3 |  |
| Dremora | EncClassDremoraMelee | 00017008 |  | 2 | 2 | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  | 2 |
| Dwarven Centurion | EncClassDwarvenCenturion | 00090356 |  | 2 |  | 3 |  | 3 |  |  |  | 1 |  |  |  |  |  |  |  |  | 2 |  |  | 3 |  | 2 |
| Dwarven Sphere | EncClassDwarvenSphere | 00090358 | 3 | 2 |  | 3 |  |  |  |  |  | 1 |  |  |  |  |  |  |  |  | 2 |  |  | 3 |  | 2 |
| Dwarven Sphere *[[sic](/wiki/UESPWiki:Spelling#Books_and_Direct_Quotes "UESPWiki:Spelling")]* | EncClassDwarvenSpider | 00090359 | 1 | 2 |  | 3 |  |  |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 3 |  | 2 |
| EbonyWarrior Class[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EbonyWarriorClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")0285c2 | 9 | 9 | 9 | 9 |  |  |  | 6 | 7 | 3 |  |  | 3 |  |  |  |  |  | 8 |  |  | 4 |  | 2 |
| Enchanter[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2NelothClassTrainer | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")017774 |  |  |  |  |  |  |  | 2 | 2 | 3 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Falmer | EncClassFalmer | 0001ce1e | 3 | 2 |  | 3 |  |  |  |  |  | 2 |  |  |  |  |  |  |  |  | 2 |  |  | 3 | 2 | 1 |
| Falmer Shaman | EncClassFalmerShaman | 0001ce1f |  |  |  | 1 |  |  |  | 2 | 1 | 3 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 3 | 1 |
| Farmer | Farmer | 0001326c | 2 |  |  | 2 | 3 | 2 |  |  |  |  | 3 |  |  |  | 3 | 1 |  |  | 1 | 1 |  | 1 | 1 | 1 |
| Fire/Frost/Shock Mage | CombatMageElemental | 0001317a |  |  |  |  |  |  |  | 2 | 2 | 3 |  |  | 3 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Fire/Frost/Shock Mage | TrainerAlterationExpert | 000e3a71 |  |  |  |  |  |  |  | 4 | 3 | 3 |  |  | 2 |  |  |  |  |  | 1 |  |  | 2 | 4 |  |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Fletcher | VendorFletcher | 00013259 | 3 |  |  |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 3 |  | 1 | 2 | 1 |
| Food Vendor | VendorFood | 00013256 |  | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 | 2 | 3 |  | 1 | 1 | 1 |
| Forsworn | EncClassForsworn | 00043bcb |  |  |  | 3 |  |  |  | 1 |  | 2 |  |  | 1 |  |  | 2 |  |  | 2 |  |  | 2 | 2 | 1 |
| Forsworn Missile | EncClassForswornMissile | 00043bcd | 3 |  |  | 1 |  |  |  | 2 |  |  |  |  | 1 |  |  | 2 |  |  | 2 |  |  | 2 | 1 | 2 |
| Forsworn Shaman | EncClassForswornShaman | 00043bcc |  |  |  |  |  |  |  | 1 | 2 | 3 |  |  | 2 |  |  | 1 |  |  | 2 |  |  | 2 | 3 |  |
| Frea Combat Style[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2csFrea | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")030cca | 1 |  |  | 3 |  |  |  | 3 |  |  |  |  | 2 |  |  | 2 |  |  |  |  |  | 3 | 1 | 2 |
| Frostbite Spider | EncClassFrostbiteSpider | 00044ccb | 3 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Gargoyle[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | DLC1EncClassGargoyle | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")00d6f6 | 2 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  |  | 4 |  | 2 |
| Giant | EncClassGiant | 000abb44 |  | 2 | 1 | 3 |  | 3 |  |  |  |  |  |  |  |  |  | 2 |  |  |  |  |  | 3 |  | 2 |
| Guard | GuardImperial | 000253f2 | 1 | 2 | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 4 |  | 2 |
| Guard | GuardSonsSkyrim | 000253f3 | 1 | 2 | 2 |  |  | 3 |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 4 | 2 |  |
| Hagraven | EncClassHagraven | 000a93b3 |  |  |  |  |  |  |  | 2 |  | 3 |  |  | 3 |  |  |  |  |  | 3 |  |  | 2 | 3 |  |
| Haknir Death-Brand[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2dunHaknirClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")037feb |  |  | 4 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  | 2 |
| Horker | EncClassHorker | 000edd36 | 3 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 5 |  | 3 |
| Horse | EncClassHorse | 0010f71e | 3 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 1 |
| Ice Wraith | EncClassIceWraith | 00073f1f | 2 | 1 |  | 2 |  |  |  |  |  | 3 |  |  |  |  |  |  |  |  | 2 |  |  | 4 |  | 2 |
| Imperial Soldier | SoldierImperialNotGuard | 0001327f | 3 | 3 | 3 | 3 |  | 3 |  |  |  |  |  |  |  |  |  | 3 |  |  |  |  |  | 3 |  | 7 |
| Jailor | Jailor | 0001325e |  | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 | 2 | 2 | 2 |  |  | 3 |  | 2 |
| Karstaag[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2dunKarstaagClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")028213 | 1 | 5 | 3 | 1 | 1 | 7 |  | 1 | 1 | 3 | 1 | 1 | 1 |  | 1 | 3 | 1 | 1 | 5 | 1 |  | 3 |  | 1 |
| Katria[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | DLC1EncClassKatria | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")004d0e | 3 | 1 | 1 | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 2 |  |  | 2 | 1 | 3 |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Lumberjack | Lumberjack | 0001326e | 2 |  |  | 2 | 3 | 2 |  |  |  |  | 3 |  |  |  | 3 | 1 |  |  | 1 | 1 |  | 1 | 1 | 1 |
| Lurker[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassLurker | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")03183a |  | 2 | 9 |  |  |  |  | 1 |  | 3 |  |  | 2 |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| Mammoth | EncClassMammoth | 000f2594 | 2 | 3 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| Miner | Miner | 0001326d | 2 |  |  | 2 | 3 | 2 |  |  |  |  | 3 |  |  |  | 3 | 1 |  |  | 1 | 1 |  | 1 | 1 | 1 |
| Miraak[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2EncClassMiraak | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")023f78 |  | 1 | 2 | 2 |  |  |  | 2 |  | 2 |  |  | 2 |  |  |  |  |  |  | 8 |  | 3 | 3 | 2 |
| Monk | CombatMonk | 00013182 | 2 |  |  | 2 |  |  |  | 2 |  |  |  |  | 2 |  |  | 1 |  |  | 2 |  |  | 2 | 2 | 2 |
| Monk | TrainerRestorationExpert | 000e3a74 |  |  |  |  |  |  |  | 3 | 1 |  |  |  | 3 |  |  |  |  |  | 2 |  |  | 2 | 3 | 1 |
| MudCrab | EncClassMudCrab | 000bb4b0 | 3 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Mystic | CombatMystic | 0001317b |  |  |  |  |  |  |  | 3 | 2 |  |  | 3 | 1 |  |  |  |  |  | 2 |  |  | 2 | 3 | 1 |
| Nightblade | CombatNightblade | 0001317c |  |  |  | 2 |  |  |  | 2 |  | 3 |  |  |  |  |  | 1 |  |  | 3 |  |  | 2 | 2 | 2 |
| Nord Hero | MQAncientNord | 0004fa49 | 2 | 2 |  | 1 |  | 3 |  |  |  |  |  |  |  |  |  | 3 |  |  |  |  |  | 4 |  | 2 |
| Orc Warrior | GuardOrc1H | 0002a477 | 2 | 1 | 3 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 4 | 2 |  |
| Orc Warrior | GuardOrc2H | 0010e714 | 2 | 1 | 3 |  |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 4 | 2 |  |
| Pawnbroker | VendorPawnbroker | 0001325b |  |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 3 |  | 1 | 1 | 1 |
| Penitus Oculatus | EncClassPenitusOculatus | 0007d98d |  | 1 | 2 | 3 |  |  |  |  |  | 2 |  |  |  |  |  |  |  |  | 1 |  |  | 2 | 2 | 2 |
| Player Spellsword Class | AAAPlayerSpellswordClass | 0002f202 | 3 | 1 |  | 2 |  |  |  |  |  | 3 |  |  | 3 |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Predator | EncClassAnimalPredator | 000131e6 | 2 | 3 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Predator | EncClassBear | 00106aed | 2 | 3 |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Prey | EncClassAnimalPrey | 0001ce1d | 3 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Priest | Priest | 00013276 |  |  |  |  | 2 |  |  |  | 2 |  | 1 |  | 3 |  | 2 |  |  |  |  | 3 |  | 1 |  | 2 |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Priest | TrainerConjurationJourneyman | 000e3a72 |  |  |  |  | 2 |  |  |  | 4 |  | 2 | 2 | 3 |  | 2 |  |  |  |  | 3 |  | 1 |  | 2 |
| Priest | TrainerEnchantingMaster | 000e3a77 |  |  |  |  | 2 |  |  |  |  | 2 | 1 |  | 3 |  | 2 |  |  |  |  | 3 |  | 1 |  | 2 |
| Priest | TrainerRestorationJourneyman | 000c2914 |  |  |  |  | 2 |  |  |  |  |  | 2 | 2 | 3 |  | 2 |  |  |  |  | 3 |  | 1 |  | 2 |
| Priest | TrainerRestorationMaster | 000e3a75 |  |  |  |  | 2 |  |  |  |  |  | 2 | 2 | 4 |  | 2 |  |  |  |  | 3 |  | 1 |  | 2 |
| Prisoner | Prisoner | 00013263 |  |  |  | 1 | 3 |  |  |  |  |  | 3 |  |  |  | 3 |  | 1 | 1 | 1 | 1 |  | 1 | 1 | 1 |
| Ranger | CombatRanger | 00013181 | 3 | 2 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 1 |  |  | 3 |  | 3 |
| Rogue | CombatRogue | 00013180 | 1 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 3 |  |  | 3 |  | 3 |
| Scout | CombatScout | 0001317d | 3 |  |  |  |  |  |  | 1 |  |  |  |  | 2 |  |  | 2 |  |  | 3 |  |  | 2 | 2 | 2 |
| Scout | TrainerSneakExpert | 000e3a6c | 3 |  |  |  |  |  |  | 1 |  |  |  |  | 2 |  |  | 2 |  |  | 4 |  |  | 2 | 2 | 2 |
| Soldier | CWSoldierClass | 0010b1d8 | 2 | 2 | 1 | 2 |  | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  |  |  |  | 3 |  | 7 |
| Sons of Skyrim Soldier | SoldierSonsSkyrimNotGuard | 00013280 | 3 | 3 | 3 | 3 |  | 3 |  |  |  |  |  |  |  |  |  | 3 |  |  |  |  |  | 1 | 1 |  |
| Sorcerer | CombatSorcerer | 00013179 |  |  | 2 | 2 |  |  |  |  |  | 3 |  | 3 | 1 |  |  |  |  |  |  |  |  | 2 | 3 | 1 |
| Sorcerer | TrainerDestructionJourneyman | 000e2fcd |  |  |  |  |  |  |  | 1 | 1 | 3 |  | 3 | 1 |  |  |  |  |  | 1 |  |  | 2 | 4 | 1 |
| Sorcerer | TrainerDestructionMaster | 000e3a73 |  |  | 2 | 2 |  |  |  | 1 |  | 3 |  |  | 3 |  |  |  |  |  |  |  |  | 3 | 3 |  |
| Sorcerer | TrainerIllusionExpert | 000b812c |  |  |  | 1 |  |  |  | 2 |  | 3 |  | 3 |  |  |  |  |  |  | 2 |  |  | 2 | 3 | 1 |
| Sorcerer | TrainerIllusionMaster | 00042dc6 |  |  | 2 | 2 |  |  |  |  |  | 3 |  | 4 | 1 |  |  |  |  |  |  |  |  | 2 | 3 | 1 |
| Sorcerer[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") | BYOHHousecarlHjaalmarchClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")019636 |  |  | 2 | 2 |  |  |  | 2 |  | 2 |  |  | 2 |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Spell Vendor | TrainerAlterationMaster | 000e3a69 |  |  |  |  |  |  |  | 4 |  | 1 |  | 2 | 1 |  |  |  |  |  | 2 | 2 |  | 1 | 1 | 1 |
| Spell Vendor | TrainerEnchantingExpert | 000e3a76 |  |  |  |  |  |  |  | 3 |  | 1 | 4 | 2 | 1 |  |  |  |  |  | 2 | 2 |  | 1 | 1 | 1 |
| Spell Vendor | VendorSpells | 0001325a |  |  |  |  |  |  |  | 3 |  | 1 |  | 2 | 1 |  |  |  |  |  | 2 | 2 |  | 1 | 1 | 1 |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Spellsword | CombatSpellsword | 00013177 |  |  | 3 | 3 |  |  |  |  |  | 3 |  |  | 2 |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Spellsword | NPCclassBelrand | 0010f7f9 |  |  |  | 3 |  |  |  |  |  | 3 |  |  | 2 |  |  | 3 |  |  |  |  |  | 2 | 2 | 2 |
| Spellsword[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | DLC2NPCClassTeldryn | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")038561 |  |  |  | 3 |  |  |  |  | 2 | 3 |  |  | 1 |  |  | 3 |  |  |  |  |  | 2 | 2 | 2 |
| Tailor | VendorTailor | 00013270 |  |  |  |  | 2 |  |  |  |  |  |  |  |  |  |  | 1 |  | 2 | 3 | 3 |  | 1 | 1 | 1 |
| Thalmor Archer | EncClassThalmorMissile | 00072891 | 3 |  |  | 1 |  |  |  |  |  |  |  |  | 1 |  |  | 2 |  |  | 2 |  |  | 2 | 1 | 2 |
| Thalmor Warrior | EncClassThalmorMelee | 0007289d |  | 2 |  | 3 |  |  |  |  |  |  |  |  | 1 |  |  | 2 |  |  | 1 |  |  | 2 | 1 | 2 |
| Thalmor Wizard | EncClassThalmorWizard | 00072887 |  |  |  |  |  |  |  | 1 | 3 | 3 |  |  | 1 |  |  |  |  |  | 1 |  |  | 2 | 3 |  |
| Thief | CombatThief | 0001317e | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  |  | 2 |  | 4 |
| Thief | TrainerLockpickMaster | 000e3a65 | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 | 4 |  | 3 |  |  | 2 |  | 4 |
| Thief | TrainerMarksmanExpert | 00042dc2 | 4 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 | 2 |  | 2 |  | 4 |
| Thief | TrainerMarksmanJourneyman | 0010fc39 | 4 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 | 2 |  | 2 |  | 4 |
| Thief | TrainerMarksmanMaster | 000e3a66 | 4 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 | 2 |  | 2 |  | 4 |
| Thief | TrainerPickpocketExpert | 000c6fb6 | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  | 3 | 3 |  |  | 2 |  | 4 |
| Thief | TrainerPickpocketMaster | 000e3a62 | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  |  | 2 |  | 4 |
| Thief | TrainerSneakMaster | 000e3a63 | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  |  | 2 |  | 4 |
| Thief | TrainerSpeechcraftMaster | 000e3a64 | 2 | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 | 4 |  | 2 |  | 4 |
| Vampire | EncClassVampire | 0002e00f |  |  |  | 2 |  |  |  | 1 | 2 | 1 |  |  |  |  |  | 2 |  |  | 3 |  |  | 2 | 2 | 1 |
| Vigilant | Vigilant1hMeleeClass | 0010bfef |  | 2 | 2 | 2 |  |  |  | 2 |  |  |  |  | 2 |  |  | 2 |  |  | 1 |  |  | 3 | 1 | 2 |
| Vigilant | Vigilant2hMeleeClass | 0010bff0 |  | 3 | 3 |  |  | 3 |  | 1 |  |  |  |  |  |  |  | 2 |  |  | 1 |  |  | 3 | 1 | 2 |
| Vyrthur[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | DLC1CClassVyrthur | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")0126b3 |  |  |  | 1 |  |  |  |  | 2 | 3 |  |  |  |  |  | 2 |  |  | 3 |  |  | 3 | 3 |  |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
| Warrior | CombatNightingale | 000fb0da | 3 |  |  | 3 |  |  |  |  |  | 2 |  |  |  |  |  | 1 |  |  | 2 |  |  | 4 |  | 2 |
| Warrior | CombatWarrior1H | 00013176 | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior | CombatWarrior2H | 0001ce15 | 2 | 2 | 3 | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior | TrainerBlockExpert | 00042dc7 |  | 3 |  | 3 | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |  | 2 | 2 | 1 |
| Warrior | TrainerBlockMaster | 000b5fb4 | 1 | 3 | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 4 | 2 | 1 |
| Warrior | TrainerLockpickExpert | 000e3a6b | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  | 4 |  |  |  |  | 4 |  | 2 |
| Warrior | TrainerOneHandedExpert | 00042dc3 | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior | TrainerOneHandedJourneyman | 000e3a5e | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior | TrainerOneHandedMaster | 000b5fb5 |  | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |  |  | 4 |  | 2 |
| Warrior | TrainerSneakJourneyman | 000e3a6d | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 4 |  | 2 |
| Warrior | TrainerSpeechcraftJourneyman | 000e3a6f | 2 | 2 | 3 | 3 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  | 4 |  | 2 |
| Warrior | TrainerTwoHandedExpert | 00042dc5 | 2 | 2 | 3 | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior | TrainerTwoHandedMaster | 00042dc4 | 2 | 2 | 3 | 1 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |  | 2 |
| Warrior[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | dlc2DBAncientDragonbornClass | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")0265af |  | 2 | 3 | 3 |  | 3 |  |  | 9 |  |  |  |  |  |  |  |  |  | 1 |  |  | 4 | 2 | 3 |
| Warrior[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | ccASVSSE001\_BladeBinder | [xx](/wiki/Skyrim:Form_ID "Skyrim:Form ID")052276 |  |  |  | 3 |  |  |  |  | 3 | 2 |  |  |  |  |  | 1 |  |  | 2 |  |  | 2 | 2 | 2 |
| Werewolf | EncClassWerewolf | 000a1993 | 2 | 2 |  | 3 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 3 |  |  | 3 |  | 3 |
| Werewolf | EncClassWerewolfBoss | 000a1995 | 1 | 2 | 2 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |  | 3 |  | 3 |
| Werewolf | EncClassWerewolfMage | 000a1994 |  | 2 |  | 3 |  |  |  |  |  | 2 |  |  |  |  |  |  |  |  | 3 |  |  | 3 | 3 |  |
| Witchblade | CombatWitchblade | 00013178 |  | 2 |  | 3 |  |  |  |  |  | 3 |  | 2 | 1 |  |  |  |  |  |  |  |  | 3 | 3 |  |
| Name | EditorID | [FormID](/wiki/Skyrim:Form_ID "Skyrim:Form ID") | [ARC](/wiki/Skyrim:Archery "Skyrim:Archery") | [BLO](/wiki/Skyrim:Block "Skyrim:Block") | [HVA](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor") | [1HD](/wiki/Skyrim:One-handed "Skyrim:One-handed") | [SMI](/wiki/Skyrim:Smithing "Skyrim:Smithing") | [2HD](/wiki/Skyrim:Two-handed "Skyrim:Two-handed") |  | [ALT](/wiki/Skyrim:Alteration "Skyrim:Alteration") | [CON](/wiki/Skyrim:Conjuration "Skyrim:Conjuration") | [DES](/wiki/Skyrim:Destruction "Skyrim:Destruction") | [ENC](/wiki/Skyrim:Enchanting "Skyrim:Enchanting") | [ILU](/wiki/Skyrim:Illusion "Skyrim:Illusion") | [RES](/wiki/Skyrim:Restoration "Skyrim:Restoration") |  | [ALC](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") | [LTA](/wiki/Skyrim:Light_Armor "Skyrim:Light Armor") | [LOC](/wiki/Skyrim:Lockpicking "Skyrim:Lockpicking") | [PIC](/wiki/Skyrim:Pickpocket "Skyrim:Pickpocket") | [SNK](/wiki/Skyrim:Sneak "Skyrim:Sneak") | [SPE](/wiki/Skyrim:Speech "Skyrim:Speech") |  | [Hea](/wiki/Skyrim:Health "Skyrim:Health") | [Mag](/wiki/Skyrim:Magicka "Skyrim:Magicka") | [Sta](/wiki/Skyrim:Stamina "Skyrim:Stamina") |
