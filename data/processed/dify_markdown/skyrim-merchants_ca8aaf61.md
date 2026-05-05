---
source_url: "https://en.uesp.net/wiki/Skyrim:Stores"
title: "Skyrim:Merchants"
entity_type: "faction"
namespace: "Skyrim"
retrieved_at: "2026-05-05T00:06:50.369713+00:00"
tags: ["All Pages Missing Data", "All Pages Needing Verification", "MetaTemplate-Load", "Skyrim-Bugs Fixed by the Official Skyrim Patch", "Skyrim-Bugs Fixed by the Official Skyrim Special Edition Patch", "Skyrim-Bugs Fixed by the Unofficial Dragonborn Patch", "Skyrim-Bugs Fixed by the Unofficial Hearthfire Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Legendary Edition Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Patch", "Skyrim-Bugs Fixed by the Unofficial Skyrim Special Edition Patch", "Skyrim-Confirmed Bugs", "Skyrim-Factions-Server", "Skyrim-Pages Missing Data", "Skyrim-Pages Needing Verification", "Skyrim-Services", "Skyrim-Unconfirmed Bugs"]
---

# Skyrim:Merchants

## Overview

[![](//images.uesp.net/thumb/0/0f/SR-npc-Lucan_Valerius.jpg/200px-SR-npc-Lucan_Valerius.jpg)](/wiki/File:SR-npc-Lucan_Valerius.jpg)

A merchant

This page summarizes all of the **merchants** available in Skyrim.

The amount listed under "Gold" is the base amount of gold that the merchant has available to purchase items from the player. Merchants will generally have 3-40 gold more than listed, because their personal pocket change is added to the merchant-specific gold. Gold is reset each time the merchant's inventory is reset or every 48 hours. Merchant gold can be increased in several ways:

- The [Master Trader](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") perk increases nearly all merchants' gold by 1000. The merchants who have more gold are all identified in the notes of the following tables.
- The [Investor](/wiki/Skyrim:Investor "Skyrim:Investor") perk allows you to invest 500 gold in certain merchants, after which that merchant will permanently have 500 more gold available. Some merchants are bugged -- they have the dialogue allowing you to pay them 500 gold, but doing so does not result in any permanent change in the merchant's available gold. These merchants are *not* checked in the "Invest" column in the following tables, but instead the bug is noted on the individual merchant page. Investing in a merchant improves that merchant's disposition towards you, which can count towards becoming a Thane in the relevant Hold, if you are on the appropriate quest to help members of that Hold.

Likewise, you can improve prices in several ways as well:

- Each rank of the [Haggling](/wiki/Skyrim:Haggling "Skyrim:Haggling") perk improves prices by 5%, beginning at 10%.
- The [Allure](/wiki/Skyrim:Allure "Skyrim:Allure") perk improves prices by 10% with merchants of the opposite gender.
- The [Lover's Insight](/wiki/Skyrim:Lover%27s_Insight "Skyrim:Lover's Insight")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") bonus from [Black Book: The Winds of Change](/wiki/Skyrim:Black_Book:_The_Winds_of_Change_(quest) "Skyrim:Black Book: The Winds of Change (quest)")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") gives 10% better prices from people of the opposite sex.
- [Fortify Barter](/wiki/Skyrim:Fortify_Barter "Skyrim:Fortify Barter") potions and enchantments improve prices by the specified amount, and potions for the specified amount of time.
- The [Blessings](/wiki/Skyrim:Blessings "Skyrim:Blessings") of Zenithar and Mephala[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") improve prices by 10% for 8 hours.
- The Blessing of Vivec[CC](/wiki/Skyrim:Creation_Club "Skyrim:Creation Club") improves prices by 5% for 8 hours.
- Leveling up your [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") skill slowly makes prices better.

The pricing formula is determined by several factors, including these:

The Base Price Factor is calculated by your Speech skill level; each skill rank reduces the price factor by .013 by default, and skill levels over 100 have no effect:

```
price factor = fBarterMax - (fBarterMax - fBarterMin) * min(skill,100)/100
price factor = 3.3 - 1.3*min(skill,100)/100
price factor = 3.3 - .013*min(skill,100)
```

- fBarterMax default is 3.3, fBarterMin default is 2.0 (defines a base vendor-selling-range of 200% to 330% of an item's base value, and a vendor-buying-range of 30% to 50%).
- the function min(x,y) return the smallest of two or more arguments (here, [skill-level] or [100]).

The modified Price Factor depends on perks and Fortify Barter bonus:

```
sell price modifier = HagglingS * AllureS * (1 + Fortify Barter from potion) * (1 + the sum of Fortify Barter from equipment + Fortify Barter from Blessing of Zenithar)
buy price modifier = HagglingB * AllureB * (1 - Fortify Barter from potion) * (1 - the sum of Fortify Barter from equipment - Fortify Barter from Blessing of Zenithar)
```

The final price combines the two Price Factors and rounds to the nearest whole number:

```
sell price = round(value of item * sell price modifier / base price factor)
buy price = round(value of item * buy price modifier * base price factor)
```

- HagglingS = 1.10 at Rank 1, 1.15 at Rank 2, 1.20 at Rank 3, 1.25 at Rank 4, 1.30 at Rank 5. AllureS = 1.10

- HagglingB = 0.91 at Rank 1, 0.87 at Rank 2, 0.83 at Rank 3, 0.80 at Rank 4, 0.77 at Rank 5. AllureB = 0.91

Buying multipliers are the reciprocal of the respective selling multiplier, but rounded to two decimal places (a percentile). Do not use unrounded (untruncated) values, as it will yield incorrect results. (For example, at rank 2, HagglingB is 0.87. 1/1.15 is actually slightly less than 0.87, so using the full (untruncated) value may get you a lower-than-actual buying multiplier.)

- At 0 skill and no perks, the final price factor is 3.3 for buying and 0.303 for selling.
- At 15 skill and no perks, the final price factor is 3.10 for buying and 0.322 for selling.
- At 100 skill and no perks, the final price factor is 2 for buying and 0.5 for selling.
- At 100 skill and all haggling perks, the final price factor is 1.54 for buying and 0.65 for selling.
- At 100 skill and all perks, including Allure, the final price factor is 1.4014 for buying and 0.715 for selling.
- Trade price cap: (max sell price = value \* 1.00), (min buy price = value \* 1.05).
  - Skill levels over 100 have no effect.

The merchandise column provides information on what type of merchandise each merchant will buy and sell. In those cases where merchants are not in a typical category, full details are provided on the specific item types they will buy and sell. However, for most merchants, one of the following categories is provided:

| Merchant Type | Buys and Sells | Notes |
| --- | --- | --- |
| Apothecaries | [Alchemy](/wiki/Skyrim:Alchemy "Skyrim:Alchemy")-related merchandise: [Animal Parts](/wiki/Skyrim:Animal_Parts "Skyrim:Animal Parts"), [Food](/wiki/Skyrim:Food "Skyrim:Food"), [Ingredients](/wiki/Skyrim:Ingredients "Skyrim:Ingredients"), [Poisons](/wiki/Skyrim:Poisons "Skyrim:Poisons"), [Potions](/wiki/Skyrim:Potions "Skyrim:Potions"), [Raw Food](/wiki/Skyrim:Raw_Food "Skyrim:Raw Food"), [Recipes](/wiki/Skyrim:Recipes "Skyrim:Recipes") |  |
| [Blacksmiths](/wiki/Skyrim:Blacksmith "Skyrim:Blacksmith") | [Animal Hides](/wiki/Skyrim:Animal_Hides "Skyrim:Animal Hides"), [Armor](/wiki/Skyrim:Armor "Skyrim:Armor"), [Arrows](/wiki/Skyrim:Ammunition "Skyrim:Ammunition"), [Ore](/wiki/Skyrim:Ore "Skyrim:Ore")/[Ingots](/wiki/Skyrim:Ingots "Skyrim:Ingots"), [Tools](/wiki/Skyrim:Tools "Skyrim:Tools"), [Weapons](/wiki/Skyrim:Weapons "Skyrim:Weapons") |  |
| [Fences](/wiki/Skyrim:Fence_(merchant) "Skyrim:Fence (merchant)") | Any items | These are only available to people who have joined the [Thieves Guild](/wiki/Skyrim:Thieves_Guild_(faction) "Skyrim:Thieves Guild (faction)"). Each Fence has a particular [quest](/wiki/Skyrim:Thieves_Guild_(faction)#Fences "Skyrim:Thieves Guild (faction)") that must be completed to make them available. Fences originally only have 1000 merchant gold, but that can be increased to 1500, 2250, 3000, and then ultimately 4000 gold by [upgrading the guild](/wiki/Skyrim:Thieves_Guild_(faction)#Upgrading_the_Thieves_Guild "Skyrim:Thieves Guild (faction)"). They are the only merchants who will purchase stolen goods, unless the [Fence](/wiki/Skyrim:Fence_(perk) "Skyrim:Fence (perk)") perk is unlocked. *Note:* Fences cannot be invested in, but are affected by the Master Trader perk |
| General Goods | Will buy any items and sell a variety of items, usually of lower value than more specific merchant types. |  |
| [Hunters](/wiki/Skyrim:Hunter "Skyrim:Hunter") | [Food](/wiki/Skyrim:Food "Skyrim:Food"), [Ingredients](/wiki/Skyrim:Ingredients "Skyrim:Ingredients") |  |
| Innkeepers | [Food](/wiki/Skyrim:Food "Skyrim:Food"), [Raw Food](/wiki/Skyrim:Raw_Food "Skyrim:Raw Food") | Innkeepers can never be invested in. |
| Jewelers | [Gems](/wiki/Skyrim:Gems "Skyrim:Gems"); [Jewelry](/wiki/Skyrim:Jewelry "Skyrim:Jewelry"); [Ore](/wiki/Skyrim:Ore "Skyrim:Ore")/[Ingots](/wiki/Skyrim:Ingots "Skyrim:Ingots"); [Tools](/wiki/Skyrim:Tools "Skyrim:Tools") | Jewelers can never be invested in, and the Master Trader perk does not affect their gold amount. |
| Spell vendors | They will both buy and sell [magic](/wiki/Skyrim:Magic "Skyrim:Magic")-related merchandise, including [spell tomes](/wiki/Skyrim:Spell_Tomes "Skyrim:Spell Tomes"), [soul gems](/wiki/Skyrim:Soul_Gems "Skyrim:Soul Gems"), enchanted [clothing](/wiki/Skyrim:Clothing "Skyrim:Clothing"), and the like. Additionally, they will buy [jewelry](/wiki/Skyrim:Jewelry "Skyrim:Jewelry"), regular clothing (but not armor), [books](/wiki/Skyrim:Books "Skyrim:Books"), [scrolls](/wiki/Skyrim:Scrolls "Skyrim:Scrolls"), [staves](/wiki/Skyrim:Staves "Skyrim:Staves"), and [Daedric artifacts](/wiki/Skyrim:Artifacts "Skyrim:Artifacts"). |  |

If the [Merchant perk](/wiki/Skyrim:Merchant_(perk) "Skyrim:Merchant (perk)") is unlocked, all merchants will purchase all types of items. The perk also makes some additional items available for purchase. All vendors will sell you items from their personal inventory, possibly including food, lockpicks, and gems. They will also sell you any bugged items that are in their merchant chests. Most notably, apothecary merchants will sell a dozen ingredients that normally they are unable to sell.

Note that outside of [Hunters](/wiki/Skyrim:Hunter "Skyrim:Hunter"), [Peddlers](/wiki/Skyrim:Peddler "Skyrim:Peddler"), and [Skooma Dealers](/wiki/Skyrim:Skooma_Dealer_(NPC) "Skyrim:Skooma Dealer (NPC)"), merchants rely on [merchant chests](/wiki/Skyrim:Merchant_Chest "Skyrim:Merchant Chest") for their merchandise, and the *chest* contains whatever [Leveled\_Lists](/wiki/Skyrim:Leveled_Lists "Skyrim:Leveled Lists") it was assigned; this is the primary reason [Investor](/wiki/Skyrim:Investor "Skyrim:Investor") and [Master Trader](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") only sometimes work, because both rely on the relevant chest containing Perk-based gold. Hence, while the merchant types listed here can be generally relied upon to determine what a merchant will buy from you, they should be regarded as guidelines, not rules, for what the merchant will sell you - for example, this is why the [Skyforge](/wiki/Skyrim:Skyforge "Skyrim:Skyforge") chest contains unique items for sale no other merchant sells, even though it is listed as a "Blacksmith" below.

Whenever two merchants are listed together in the following tables, it means that the two merchants share the same [merchant chest](/wiki/Skyrim:Merchant_Chest "Skyrim:Merchant Chest"). Therefore, the merchants will always provide the exact same list of items, and share the same merchant gold. If one of the people is listed in parentheses, that person only takes over the store if the first person dies. Investing in a store with two merchants, or with successive merchants, will increase the available amount of gold for all merchants, but may only improve the disposition of one (this is particularly noticeable at Radiant Raiment with the Altmer sisters Endarie and Taarie.)

Most merchants are open from around 8am to 8pm, but some are open all day. For instance, most blacksmiths are only open during the day, whereas innkeepers are always open.

You can also ask four [children](/wiki/Skyrim:Child "Skyrim:Child") what they have for sale. None of them can be invested in, though, and Babette is the only one whose shop benefits from the Master Trader perk.

A merchant's inventory will be determined by an item generator; such that each separate save or character created from that save will yield completely different results every time. If you have the [Special Edition](/wiki/Skyrim:Special_Edition "Skyrim:Special Edition"), quicksaving before entering a shop will do the same.

If you are [married](/wiki/Skyrim:Marriage "Skyrim:Marriage") then your spouse will open a store, whose merchant chest is located inside the home where your spouse lives. If your spouse is on the list below, then they will continue to sell the same type of items. Otherwise, your spouse will become a general goods trader.

### Windhelm

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Ambarys Rendar](/wiki/Skyrim:Ambarys_Rendar "Skyrim:Ambarys Rendar") | [New Gnisis Cornerclub](/wiki/Skyrim:New_Gnisis_Cornerclub "Skyrim:New Gnisis Cornerclub") | Innkeeper | **100** | ☒ | ☑ |
| [Aval Atheron](/wiki/Skyrim:Aval_Atheron "Skyrim:Aval Atheron") | Marketplace Stall | General | **50** | ☒ | ☑ |
| [Elda Early-Dawn](/wiki/Skyrim:Elda_Early-Dawn "Skyrim:Elda Early-Dawn") ([Nils](/wiki/Skyrim:Nils "Skyrim:Nils")) | [Candlehearth Hall](/wiki/Skyrim:Candlehearth_Hall "Skyrim:Candlehearth Hall") | Innkeeper | **100** | ☒ | ☑ |
| [Hillevi Cruel-Sea](/wiki/Skyrim:Hillevi_Cruel-Sea "Skyrim:Hillevi Cruel-Sea") | Marketplace Stall | Innkeeper | **50** | ☒ | ☑ |
| [Niranye](/wiki/Skyrim:Niranye "Skyrim:Niranye") | [Niranye's House](/wiki/Skyrim:Niranye%27s_House "Skyrim:Niranye's House") | Fence | **1000**-**4000** | ☒ | ☑ |
| Marketplace Stall | General | **750** |
| [Nurelion](/wiki/Skyrim:Nurelion "Skyrim:Nurelion") ([Quintus Navale](/wiki/Skyrim:Quintus_Navale "Skyrim:Quintus Navale")) | [The White Phial](/wiki/Skyrim:The_White_Phial_(place) "Skyrim:The White Phial (place)") | Apothecary | **500** | ☑ | ☑ |
| [Oengul War-Anvil](/wiki/Skyrim:Oengul_War-Anvil "Skyrim:Oengul War-Anvil") ([Hermir Strong-Heart](/wiki/Skyrim:Hermir_Strong-Heart "Skyrim:Hermir Strong-Heart")) | [Blacksmith Quarters](/wiki/Skyrim:Blacksmith_Quarters "Skyrim:Blacksmith Quarters") | Blacksmith | **1000** | ☑ | ☑ |
| [Revyn Sadri](/wiki/Skyrim:Revyn_Sadri "Skyrim:Revyn Sadri") | [Sadri's Used Wares](/wiki/Skyrim:Sadri%27s_Used_Wares "Skyrim:Sadri's Used Wares") | General | **750** | ☑ | ☑ |
| [Sofie](/wiki/Skyrim:Sofie "Skyrim:Sofie")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") | Windhelm Gate | Flowers (also sells [flower baskets](/wiki/Skyrim:Flower_Basket "Skyrim:Flower Basket")) | **50** | ☒ | ☒ |
| [Ulundil](/wiki/Skyrim:Ulundil "Skyrim:Ulundil") ([Arivanya](/wiki/Skyrim:Arivanya "Skyrim:Arivanya")) | [Windhelm Stables](/wiki/Skyrim:Windhelm_Stables "Skyrim:Windhelm Stables") | [Horses](/wiki/Skyrim:Horses "Skyrim:Horses") |  | ☒ |  |
| [Wuunferth the Unliving](/wiki/Skyrim:Wuunferth_the_Unliving "Skyrim:Wuunferth the Unliving") | [Palace of the Kings](/wiki/Skyrim:Palace_of_the_Kings "Skyrim:Palace of the Kings") | Spells | **500** | ☑ | ☑ |

- Sofie will stop selling flowers and flower baskets if you [adopt](/wiki/Skyrim:Adoption "Skyrim:Adoption") her.
- Hermir's bartering dialogue has no audio as her voice type does not support the specific blacksmith bartering lines.

#### Bugs

- [Dravynea the Stoneweaver](/wiki/Skyrim:Dravynea_the_Stoneweaver "Skyrim:Dravynea the Stoneweaver") was supposed to be the backup vendor for Wuunferth if he died, but the vendor data was not set up correctly.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.2, fixes this bug.
- [Malthyr Elenil](/wiki/Skyrim:Malthyr_Elenil "Skyrim:Malthyr Elenil") is set up to sell drinks at New Gnisis Cornerclub if Ambrys Rendar dies, but cannot due to a developer oversight.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.2, addresses this issue. Malthyr will now be able to sell drinks there.
- [Susanna the Wicked](/wiki/Skyrim:Susanna_the_Wicked "Skyrim:Susanna the Wicked") is set up to sell drinks at Candlehearth Hall, but doesn't because she was never added to the appropriate faction.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.2, addresses this issue. Susanna will now be able to sell drinks there.
  - Be warned, however, that once [Blood on the Ice](/wiki/Skyrim:Blood_on_the_Ice "Skyrim:Blood on the Ice") has begun, Susanna's services will be permanently unavailable, regardless if you have the Unofficial Patch or not.
- If Revyn Sadri dies, Aval Atheron is supposed to take over as the new shopkeeper at Sadri's Used Wares. Unfortunately, Aval has his own market stall and therefore cannot actually take over the shop.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.4, addresses this issue. [Idesa Sadri](/wiki/Skyrim:Idesa_Sadri "Skyrim:Idesa Sadri") has been selected to fill the backup alias and will now take over if Revyn is dead.
- Due to a scripting error, Sofie would end up overloading her merchant inventory with flower baskets. This script polled every 10 seconds while she was loaded and could in theory result in her having enough baskets to overflow the reference counts.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch"), version 3.0.1, addresses this issue. This script has now been removed, and her AI package has been modified to instead play the idle continuously. In addition, the AI pack script will slowly remove the baskets over time as they are not needed for her schedule to function.
- Despite only having meat on display at his stall, Aval Atheron actually deals in miscellaneous goods, similar to pawnbrokers.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.9, addresses this issue. He will now only sell goods similar to those on display.
- Aval Atheron's line about his "fresh fruits and vegetables" makes little sense in accordance with his actual merchandise.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.6, addresses this issue. The line has now been completely blocked from playing.

### Outside Towns

| Merchant Name | Store Name | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Bolar](/wiki/Skyrim:Bolar "Skyrim:Bolar") | at [Mauhulakh's Longhouse](/wiki/Skyrim:Mauhulakh%27s_Longhouse "Skyrim:Mauhulakh's Longhouse") | [Narzulbur](/wiki/Skyrim:Narzulbur "Skyrim:Narzulbur") | Apothecary | **500** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Dushnamub](/wiki/Skyrim:Dushnamub "Skyrim:Dushnamub") | at [Mauhulakh's Longhouse](/wiki/Skyrim:Mauhulakh%27s_Longhouse "Skyrim:Mauhulakh's Longhouse") | [Narzulbur](/wiki/Skyrim:Narzulbur "Skyrim:Narzulbur") | Blacksmith | **400** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Iddra](/wiki/Skyrim:Iddra "Skyrim:Iddra") | [Braidwood Inn](/wiki/Skyrim:Braidwood_Inn "Skyrim:Braidwood Inn") | [Kynesgrove](/wiki/Skyrim:Kynesgrove "Skyrim:Kynesgrove") | Innkeeper | **100** | ☒ |  |  |
| [Gilfre](/wiki/Skyrim:Gilfre "Skyrim:Gilfre") |  | [Mixwater Mill](/wiki/Skyrim:Mixwater_Mill "Skyrim:Mixwater Mill") | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |  |

#### Bugs

- If anything happens to Iddra, [Kjeld](/wiki/Skyrim:Kjeld "Skyrim:Kjeld") will take over room rentals, but not merchant services. In the absence of Iddra, it is impossible to buy or sell things in Kynesgrove.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.4, addresses this issue. Kjeld can now sell innkeeper merchandise as well if he takes over as the publican of Braidwood Inn.

### Falkreath

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Babette](/wiki/Skyrim:Babette "Skyrim:Babette") | in the [Dark Brotherhood Sanctuary](/wiki/Skyrim:Dark_Brotherhood_Sanctuary "Skyrim:Dark Brotherhood Sanctuary") (see note below) | Apothecary (also sells [Tools](/wiki/Skyrim:Tools "Skyrim:Tools")) | **500** | ☒ | ☑ |
| [Bolund](/wiki/Skyrim:Bolund "Skyrim:Bolund") | Falkreath sawmill | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |
| [Solaf](/wiki/Skyrim:Solaf "Skyrim:Solaf") | [Gray Pine Goods](/wiki/Skyrim:Gray_Pine_Goods "Skyrim:Gray Pine Goods") | General; sells [Blue Mage Robes](/wiki/Skyrim:Blue_Mage_Robes "Skyrim:Blue Mage Robes") | **750** | ☑ | ☑ |
| [Lod](/wiki/Skyrim:Lod "Skyrim:Lod") | [Lod's House](/wiki/Skyrim:Lod%27s_House "Skyrim:Lod's House") | Blacksmith | **1000** | ☒(☑) | ☑ |
| [Valga Vinicia](/wiki/Skyrim:Valga_Vinicia "Skyrim:Valga Vinicia") | [Dead Man's Drink](/wiki/Skyrim:Dead_Man%27s_Drink "Skyrim:Dead Man's Drink") | Innkeeper | **100** | ☒ |  |
| [Zaria](/wiki/Skyrim:Zaria "Skyrim:Zaria") | [Grave Concoctions](/wiki/Skyrim:Grave_Concoctions "Skyrim:Grave Concoctions") | Apothecary | **500** | ☒(☑) | ☑ |

- Babette will no longer be present in the Dark Brotherhood Sanctuary if you finish the [Dark Brotherhood](/wiki/Skyrim:Dark_Brotherhood "Skyrim:Dark Brotherhood") questline, as it will eventually be destroyed.
  - If you start [Destroy the Dark Brotherhood!](/wiki/Skyrim:Destroy_the_Dark_Brotherhood! "Skyrim:Destroy the Dark Brotherhood!") instead, she won't be there at all.
- Lod and Zaria are not investable due to a bug. The Unofficial Skyrim Special Edition Patch fixes this bug.

### Other Locations

| Merchant Name | Store Name | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- | --- |
| [Hert](/wiki/Skyrim:Hert "Skyrim:Hert") |  | [Half-Moon Mill](/wiki/Skyrim:Half-Moon_Mill "Skyrim:Half-Moon Mill") | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |

### Bugs

- [Narri](/wiki/Skyrim:Narri "Skyrim:Narri"), as part of the [Server](/wiki/Skyrim:Server "Skyrim:Server") faction, is supposed to trigger the option to buy food from her menu when you take a seat inside Dead Man's Drink; however, due to her not being in the correct factions, no such option is available, so she'll keep asking you if you would like something to eat, with no possibility to reply.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.1, fixes this bug.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://en.wikipedia.org/wiki/PC_game "PC") To fix this, add her to the Dead Man's Drink faction by targeting her and using the console command `addtofaction 000a6bfb 1`.
- Narri was meant to take over Dead Man's Drink in case something happened to Valga Vinicia, but she can't due to a backup alias not being defined properly.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.2, fixes this bug.

### Solitude

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Addvar](/wiki/Skyrim:Addvar "Skyrim:Addvar") ([Greta](/wiki/Skyrim:Greta "Skyrim:Greta")) | Marketplace Stall | Innkeeper | **50** | ☒ | ☑ |
| [Angeline Morrard](/wiki/Skyrim:Angeline_Morrard "Skyrim:Angeline Morrard") ([Vivienne Onis](/wiki/Skyrim:Vivienne_Onis "Skyrim:Vivienne Onis")) | [Angeline's Aromatics](/wiki/Skyrim:Angeline%27s_Aromatics "Skyrim:Angeline's Aromatics") | Apothecary | **500** | ☒(☑)[†](#intnote_Angeline) | ☑ |
| [Beirand](/wiki/Skyrim:Beirand "Skyrim:Beirand") | [Solitude Blacksmith](/wiki/Skyrim:Solitude_Blacksmith "Skyrim:Solitude Blacksmith") | Blacksmith | **1000** | ☑ | ☑ |
| [Corpulus Vinius](/wiki/Skyrim:Corpulus_Vinius "Skyrim:Corpulus Vinius") | [The Winking Skeever](/wiki/Skyrim:The_Winking_Skeever "Skyrim:The Winking Skeever") | Innkeeper | **100** | ☒ | ☑ |
| [Endarie](/wiki/Skyrim:Endarie "Skyrim:Endarie"); [Taarie](/wiki/Skyrim:Taarie "Skyrim:Taarie") | [Radiant Raiment](/wiki/Skyrim:Radiant_Raiment "Skyrim:Radiant Raiment") | [Clothing](/wiki/Skyrim:Clothing "Skyrim:Clothing"), [Jewelry](/wiki/Skyrim:Jewelry "Skyrim:Jewelry") | **750** | ☑ | ☑ |
| [Evette San](/wiki/Skyrim:Evette_San "Skyrim:Evette San") | Marketplace Stall | Innkeeper | **50** | ☒ | ☑ |
| [Fihada](/wiki/Skyrim:Fihada "Skyrim:Fihada") ([Jawanan](/wiki/Skyrim:Jawanan "Skyrim:Jawanan")) | [Fletcher](/wiki/Skyrim:Fletcher_(place) "Skyrim:Fletcher (place)") | [Armor](/wiki/Skyrim:Armor "Skyrim:Armor"), [Arrows](/wiki/Skyrim:Arrows "Skyrim:Arrows"), [Tools](/wiki/Skyrim:Tools "Skyrim:Tools"), [Weapons](/wiki/Skyrim:Weapons "Skyrim:Weapons") | **750** | ☒(☑)[†](#intnote_Fihada) | ☑ |
| [Geimund](/wiki/Skyrim:Geimund "Skyrim:Geimund") ([Horm](/wiki/Skyrim:Horm "Skyrim:Horm")) | [Solitude Stables](/wiki/Skyrim:Solitude_Stables "Skyrim:Solitude Stables") (via [Katla's Farm](/wiki/Skyrim:Katla%27s_Farm "Skyrim:Katla's Farm")) | [Horses](/wiki/Skyrim:Horses "Skyrim:Horses") |  | ☒ |  |
| [Gulum-Ei](/wiki/Skyrim:Gulum-Ei "Skyrim:Gulum-Ei") | [The Winking Skeever](/wiki/Skyrim:The_Winking_Skeever "Skyrim:The Winking Skeever") | Fence | **1000**-**4000** | ☒ | ☑ |
| [Jala](/wiki/Skyrim:Jala "Skyrim:Jala") | Marketplace Stall | Innkeeper | **50** | ☒ | ☑ |
| [Sayma](/wiki/Skyrim:Sayma "Skyrim:Sayma") | [Bits and Pieces](/wiki/Skyrim:Bits_and_Pieces "Skyrim:Bits and Pieces") | General | **750** | ☑ | ☑ |
| [Sybille Stentor](/wiki/Skyrim:Sybille_Stentor "Skyrim:Sybille Stentor") ([Melaran](/wiki/Skyrim:Melaran "Skyrim:Melaran")) | [Blue Palace](/wiki/Skyrim:Blue_Palace "Skyrim:Blue Palace") | Spells | **500** | ☑ | ☑ |

[†](#note_Angeline)It is possible to invest endlessly with [Angeline](/wiki/Skyrim:Angeline_Morrard "Skyrim:Angeline Morrard"). She never loses the dialogue option to invest, but her permanent base gold cannot increase, due to a [bug](/wiki/Skyrim:Angeline_Morrard#Bugs "Skyrim:Angeline Morrard").

- This is fixed by the Unofficial Skyrim Patch (both Legendary and Special Edition versions).
- You can use the console command `set PerkInvestorSolitudeApothecary to 0` to invest in Angeline's store.

[†](#note_Fihada)A similar bug prevents investing with [Fihada](/wiki/Skyrim:Fihada "Skyrim:Fihada").

- This is fixed by the Unofficial Skyrim Patch (both Legendary and Special Edition versions).
- No easy fix from the console exists.[*verification needed — but maybe there's a combination of commands that works?*]

#### Bugs

- [Heimvar](/wiki/Skyrim:Heimvar "Skyrim:Heimvar") is supposed to replace Beirand if something happens to him. Unfortunately, he doesn't sell anything, as he isn't set up properly to do that.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2, fixes this bug.
- Despite supposedly being Sybille Stentor's replacement as Court Wizard in the event of her death, Melaran will not change his routine or sell anything to reflect this.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2, fixes this bug.
- After [Scoundrel's Folly](/wiki/Skyrim:Scoundrel%27s_Folly "Skyrim:Scoundrel's Folly"), Gulum-Ei is supposed to begin fencing goods but is unable to do so because his chest's enable parent setup is wrong.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.3, fixes this bug.
- [Vittoria Vici](/wiki/Skyrim:Vittoria_Vici "Skyrim:Vittoria Vici") was supposed to offer services as a general merchant when down at the docks, but she instead just stands there without the option to trade with her.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.4, fixes this bug.
- If you buy a horse from Katla's Farm and the horse is killed, attempting to purchase a new horse from the same stable results in 1000 gold being deducted, and Geimund stating that your horse is "the one with the saddle", despite no saddled horse appearing at the stables there. Instead, the new horse spawns at the [Riften Stables](/wiki/Skyrim:Riften_Stables "Skyrim:Riften Stables").
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.5, fixes this bug.
- Selling crops to [Katla](/wiki/Skyrim:Katla "Skyrim:Katla") will allow you to ride the horses at Solitude Stables for free, due to her being in the same ownership faction as the stablemaster. The problem is that horses cost 1,000 gold, making them way too valuable to let stablemasters let you ride them for free after completing a small favor.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.1.2, addresses this issue. ([details](https://afktrack.afkmods.com/index.php?a=issues&i=19062)) The ownership of the horses was changed to just Geimund, rather than the faction, preventing this issue.

### Other Locations

| Merchant Name | Store Name | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Faida](/wiki/Skyrim:Faida "Skyrim:Faida") | [Four Shields Tavern](/wiki/Skyrim:Four_Shields_Tavern "Skyrim:Four Shields Tavern") | [Dragon Bridge](/wiki/Skyrim:Dragon_Bridge "Skyrim:Dragon Bridge") | Innkeeper | **100** | ☒ |  |  |
| [Kharag gro-Shurkul](/wiki/Skyrim:Kharag_gro-Shurkul "Skyrim:Kharag gro-Shurkul") |  | [Solitude Sawmill](/wiki/Skyrim:Solitude_Sawmill "Skyrim:Solitude Sawmill") | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |  |
| [Feran Sadri](/wiki/Skyrim:Feran_Sadri "Skyrim:Feran Sadri")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Volkihar Keep](/wiki/Skyrim:Volkihar_Keep "Skyrim:Volkihar Keep")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Apothecary | **500** | ☒ | ☒ | Hostile to non-vampires |
| [Hestla](/wiki/Skyrim:Hestla "Skyrim:Hestla")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Volkihar Keep](/wiki/Skyrim:Volkihar_Keep "Skyrim:Volkihar Keep")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Blacksmith | **1000** | ☒ | ☒ | Hostile to non-vampires |
| [Ronthil](/wiki/Skyrim:Ronthil "Skyrim:Ronthil")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Volkihar Keep](/wiki/Skyrim:Volkihar_Keep "Skyrim:Volkihar Keep")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | General | **750** | ☒ | ☒ | Hostile to non-vampires |

#### Bugs

- [Julienne Lylvieve](/wiki/Skyrim:Julienne_Lylvieve "Skyrim:Julienne Lylvieve") was meant to be Faida's backup for the Four Shields Tavern, but isn't because there is no backup alias.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.2, fixes this bug.

### Morthal

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Falion](/wiki/Skyrim:Falion "Skyrim:Falion") | [Falion's House](/wiki/Skyrim:Falion%27s_House "Skyrim:Falion's House") | Spells; sells 1 [Black Soul Gem](/wiki/Skyrim:Black_Soul_Gem "Skyrim:Black Soul Gem") | **500** | ☒(☑) | ☑ | [Cures vampirism](/wiki/Skyrim:Rising_at_Dawn "Skyrim:Rising at Dawn") |
| [Jonna](/wiki/Skyrim:Jonna "Skyrim:Jonna") | [Moorside Inn](/wiki/Skyrim:Moorside_Inn "Skyrim:Moorside Inn") | Innkeeper | **100** | ☒ |  |  |
| [Lami](/wiki/Skyrim:Lami "Skyrim:Lami") | [Thaumaturgist's Hut](/wiki/Skyrim:Thaumaturgist%27s_Hut "Skyrim:Thaumaturgist's Hut") | Apothecary | **500** | ☑ | ☑ |  |
| [Thonnir](/wiki/Skyrim:Thonnir "Skyrim:Thonnir") | Morthal sawmill | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |  |

- Falion is investable with the most recent Unofficial Skyrim Special Edition Patch.

### Dawnstar

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Babette](/wiki/Skyrim:Babette "Skyrim:Babette") | in the [Dawnstar Sanctuary](/wiki/Skyrim:Dawnstar_Sanctuary "Skyrim:Dawnstar Sanctuary") (see note below) | Apothecary (also sells [Tools](/wiki/Skyrim:Tools "Skyrim:Tools")) | **500** | ☒ | ☑ |
| [Frida](/wiki/Skyrim:Frida "Skyrim:Frida") | [The Mortar and Pestle](/wiki/Skyrim:The_Mortar_and_Pestle "Skyrim:The Mortar and Pestle") | Apothecary | **500** | ☑ | ☑ |
| [Thoring](/wiki/Skyrim:Thoring "Skyrim:Thoring") ([Karita](/wiki/Skyrim:Karita_(bard) "Skyrim:Karita (bard)")) | [Windpeak Inn](/wiki/Skyrim:Windpeak_Inn "Skyrim:Windpeak Inn") | Innkeeper | **100** | ☒ |  |
| [Madena](/wiki/Skyrim:Madena "Skyrim:Madena") | [The White Hall](/wiki/Skyrim:The_White_Hall "Skyrim:The White Hall") | Spells | **500** |  | ☑ |
| [Rustleif](/wiki/Skyrim:Rustleif "Skyrim:Rustleif"); [Seren](/wiki/Skyrim:Seren "Skyrim:Seren") | [Rustleif's House](/wiki/Skyrim:Rustleif%27s_House "Skyrim:Rustleif's House") | Blacksmith | **1000** | ☑ | ☑ |

- Babette is only available in the Dawnstar Sanctuary if you finish the [Dark Brotherhood](/wiki/Skyrim:Dark_Brotherhood "Skyrim:Dark Brotherhood") questline.

### Other Locations

| Merchant Name | Store Name | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- | --- |
| [Aeri](/wiki/Skyrim:Aeri "Skyrim:Aeri") |  | [Anga's Mill](/wiki/Skyrim:Anga%27s_Mill "Skyrim:Anga's Mill") | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |
| [Agrane Peryval](/wiki/Skyrim:Agrane_Peryval "Skyrim:Agrane Peryval")[CC](/wiki/Skyrim:Saturalia_Holiday_Pack "Skyrim:Saturalia Holiday Pack") |  | Camp north of [Windward Ruins](/wiki/Skyrim:Windward_Ruins "Skyrim:Windward Ruins") | Unique holiday gear | **750** |  | ☑ |
| [Hadring](/wiki/Skyrim:Hadring "Skyrim:Hadring") |  | [Nightgate Inn](/wiki/Skyrim:Nightgate_Inn "Skyrim:Nightgate Inn") | Innkeeper | **100** | ☒ |  |

### Markarth

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Anton Virane](/wiki/Skyrim:Anton_Virane "Skyrim:Anton Virane") | in [Understone Keep](/wiki/Skyrim:Understone_Keep "Skyrim:Understone Keep") | Innkeeper | **100** | ☒ |  |
| [Bothela](/wiki/Skyrim:Bothela "Skyrim:Bothela") ([Muiri](/wiki/Skyrim:Muiri "Skyrim:Muiri")) | [The Hag's Cure](/wiki/Skyrim:The_Hag%27s_Cure "Skyrim:The Hag's Cure") | Apothecary | **500** | ☑ | ☑ |
| [Calcelmo](/wiki/Skyrim:Calcelmo "Skyrim:Calcelmo") | in [Understone Keep](/wiki/Skyrim:Understone_Keep "Skyrim:Understone Keep") | Spells | **500** | ☑ | ☑ |
| [Cedran](/wiki/Skyrim:Cedran "Skyrim:Cedran"); [Banning](/wiki/Skyrim:Banning "Skyrim:Banning") | [Markarth Stables](/wiki/Skyrim:Markarth_Stables "Skyrim:Markarth Stables") | [Horses](/wiki/Skyrim:Horses "Skyrim:Horses") (Cedran) War Dogs (Banning) |  | ☒ |  |
| [Kleppr](/wiki/Skyrim:Kleppr "Skyrim:Kleppr") ([Frabbi](/wiki/Skyrim:Frabbi "Skyrim:Frabbi")) | [Silver-Blood Inn](/wiki/Skyrim:Silver-Blood_Inn "Skyrim:Silver-Blood Inn") | Innkeeper | **100** | ☒ |  |
| [Endon](/wiki/Skyrim:Endon "Skyrim:Endon") | [Endon's House](/wiki/Skyrim:Endon%27s_House "Skyrim:Endon's House") or in [Silver-Blood Inn](/wiki/Skyrim:Silver-Blood_Inn "Skyrim:Silver-Blood Inn") | Fence | **1000**-**4000** | ☒ | ☑ |
| [Ghorza gra-Bagol](/wiki/Skyrim:Ghorza_gra-Bagol "Skyrim:Ghorza gra-Bagol") ([Tacitus Sallustius](/wiki/Skyrim:Tacitus_Sallustius "Skyrim:Tacitus Sallustius")) | at the forge near [The Hag's Cure](/wiki/Skyrim:The_Hag%27s_Cure "Skyrim:The Hag's Cure") or in [Understone Keep](/wiki/Skyrim:Understone_Keep "Skyrim:Understone Keep") | Blacksmith | **1000** | ☒(☑)[†](#intnote_GhorzaMoth) | ☑ |
| [Hogni Red-Arm](/wiki/Skyrim:Hogni_Red-Arm "Skyrim:Hogni Red-Arm") | Marketplace Stall | Innkeeper | **50** | ☒ |  |
| [Kerah](/wiki/Skyrim:Kerah "Skyrim:Kerah") | Marketplace Stall | Jeweler | **50** | ☒ | ☒ |
| [Lisbet](/wiki/Skyrim:Lisbet "Skyrim:Lisbet") ([Imedhnain](/wiki/Skyrim:Imedhnain "Skyrim:Imedhnain")) | [Arnleif and Sons Trading Company](/wiki/Skyrim:Arnleif_and_Sons_Trading_Company "Skyrim:Arnleif and Sons Trading Company") | General | **750** | ☑ | ☑ |
| [Moth gro-Bagol](/wiki/Skyrim:Moth_gro-Bagol "Skyrim:Moth gro-Bagol") | in [Understone Keep](/wiki/Skyrim:Understone_Keep "Skyrim:Understone Keep") | Blacksmith | **500** | ☑[†](#intnote_GhorzaMoth) | ☑ |

- If either Cedran or Banning dies, then the survivor will NOT take over his mate's services: you cannot end up buying a dog from Cedran or a horse from Banning.

[†](#note_GhorzaMoth)Ghorza gra-Bagol will have the dialogue option to invest in her store, but the only option is to decline, due to a [bug](/wiki/Skyrim:Ghorza_gra-Bagol#Bugs "Skyrim:Ghorza gra-Bagol"). If she dies, however, you can invest in her successor, Tacitus Sallustius. Investing in either one (after having fixed the bug mentioned above) also invests 500 gold in [Moth gro-Bagol](/wiki/Skyrim:Moth_gro-Bagol "Skyrim:Moth gro-Bagol"), due to [another bug](/wiki/Skyrim:Ghorza_gra-Bagol#Bugs "Skyrim:Ghorza gra-Bagol").

:   [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://en.wikipedia.org/wiki/PC_game "PC") Both bugs are fixed by the current version of the [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch").

    - You can use the console command `set PerkInvestorMarkarthBlacksmith to 0` to invest in both blacksmiths.

### Other Locations

| Merchant Name | Store Place | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Gharol](/wiki/Skyrim:Gharol "Skyrim:Gharol") | at [Burguk's Longhouse](/wiki/Skyrim:Burguk%27s_Longhouse "Skyrim:Burguk's Longhouse") | [Dushnikh Yal](/wiki/Skyrim:Dushnikh_Yal "Skyrim:Dushnikh Yal") | Blacksmith | **400** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Murbul](/wiki/Skyrim:Murbul "Skyrim:Murbul") | at [Burguk's Longhouse](/wiki/Skyrim:Burguk%27s_Longhouse "Skyrim:Burguk's Longhouse") | [Dushnikh Yal](/wiki/Skyrim:Dushnikh_Yal "Skyrim:Dushnikh Yal") | Apothecary | **500** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Sharamph](/wiki/Skyrim:Sharamph "Skyrim:Sharamph") | at [Larak's Longhouse](/wiki/Skyrim:Larak%27s_Longhouse "Skyrim:Larak's Longhouse") | [Mor Khazgur](/wiki/Skyrim:Mor_Khazgur "Skyrim:Mor Khazgur") | Apothecary | **500** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Shuftharz](/wiki/Skyrim:Shuftharz "Skyrim:Shuftharz") | at [Larak's Longhouse](/wiki/Skyrim:Larak%27s_Longhouse "Skyrim:Larak's Longhouse") | [Mor Khazgur](/wiki/Skyrim:Mor_Khazgur "Skyrim:Mor Khazgur") | Blacksmith | **400** |  | ☑ | Only available if you are [Blood-Kin](/wiki/Skyrim:Blood-Kin "Skyrim:Blood-Kin") |
| [Eydis](/wiki/Skyrim:Eydis "Skyrim:Eydis"); [Skuli](/wiki/Skyrim:Skuli "Skyrim:Skuli") ([Leontius Salvius](/wiki/Skyrim:Leontius_Salvius "Skyrim:Leontius Salvius")) |  | [Old Hroldan Inn](/wiki/Skyrim:Old_Hroldan_Inn "Skyrim:Old Hroldan Inn") | Innkeeper | **100** | ☒ |  |  |

### Riften

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Arnskar Ember-Master](/wiki/Skyrim:Arnskar_Ember-Master "Skyrim:Arnskar Ember-Master") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Blacksmith | **1000** | ☒ | ☑ |
| [Balimund](/wiki/Skyrim:Balimund "Skyrim:Balimund") ([Asbjorn Fire-Tamer](/wiki/Skyrim:Asbjorn_Fire-Tamer "Skyrim:Asbjorn Fire-Tamer")) | [The Scorched Hammer](/wiki/Skyrim:The_Scorched_Hammer "Skyrim:The Scorched Hammer") | Blacksmith | **1000** | ☑ | ☑ |
| [Bersi Honey-Hand](/wiki/Skyrim:Bersi_Honey-Hand "Skyrim:Bersi Honey-Hand") ([Drifa](/wiki/Skyrim:Drifa "Skyrim:Drifa")) | [Pawned Prawn](/wiki/Skyrim:Pawned_Prawn "Skyrim:Pawned Prawn") | General | **750** | ☑ | ☑ |
| [Brand-Shei](/wiki/Skyrim:Brand-Shei "Skyrim:Brand-Shei") | Marketplace Stall | General | **750** | ☒(☑[†](#intnote_Brand-SheiGrelkaMadesiMarise)) | ☑ |
| [Vekel the Man](/wiki/Skyrim:Vekel_the_Man "Skyrim:Vekel the Man") ([Dirge](/wiki/Skyrim:Dirge "Skyrim:Dirge")) | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Innkeeper | **100** | ☒ | ☒ |
| [Elgrim](/wiki/Skyrim:Elgrim "Skyrim:Elgrim"); [Hafjorg](/wiki/Skyrim:Hafjorg "Skyrim:Hafjorg") | [Elgrim's Elixirs](/wiki/Skyrim:Elgrim%27s_Elixirs "Skyrim:Elgrim's Elixirs") | Apothecary | **500** | ☑ | ☑ |
| [Galathil](/wiki/Skyrim:Galathil "Skyrim:Galathil")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Facial Reconstruction | **N/A** | ☒ | ☒ |
| [Grelka](/wiki/Skyrim:Grelka "Skyrim:Grelka") | Marketplace Stall | General | **750** | ☒(☑[†](#intnote_Brand-SheiGrelkaMadesiMarise)) | ☑ |
| [Herluin Lothaire](/wiki/Skyrim:Herluin_Lothaire "Skyrim:Herluin Lothaire") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Apothecary | **500** | ☒ | ☑ |
| [Hofgrir Horse-Crusher](/wiki/Skyrim:Hofgrir_Horse-Crusher "Skyrim:Hofgrir Horse-Crusher") ([Shadr)](/wiki/Skyrim:Shadr "Skyrim:Shadr") | [Riften Stables](/wiki/Skyrim:Riften_Stables "Skyrim:Riften Stables") | [Horses](/wiki/Skyrim:Horses "Skyrim:Horses") |  | ☒ |  |
| [Ungrien](/wiki/Skyrim:Ungrien "Skyrim:Ungrien") | [Black-Briar Meadery](/wiki/Skyrim:Black-Briar_Meadery "Skyrim:Black-Briar Meadery") | Innkeeper | **100** | ☒ |  |
| [Romlyn Dreth](/wiki/Skyrim:Romlyn_Dreth "Skyrim:Romlyn Dreth") | [Black-Briar Meadery](/wiki/Skyrim:Black-Briar_Meadery "Skyrim:Black-Briar Meadery") | [Black-Briar Mead](/wiki/Skyrim:Black-Briar_Mead "Skyrim:Black-Briar Mead") |  | ☒ |  |
| [Keerava](/wiki/Skyrim:Keerava "Skyrim:Keerava"); [Talen-Jei](/wiki/Skyrim:Talen-Jei "Skyrim:Talen-Jei") | [The Bee and Barb](/wiki/Skyrim:The_Bee_and_Barb "Skyrim:The Bee and Barb") | Innkeeper | **100** | ☒ |  |
| [Maramal](/wiki/Skyrim:Maramal "Skyrim:Maramal") | [Temple of Mara](/wiki/Skyrim:Temple_of_Mara "Skyrim:Temple of Mara") | [Amulet of Mara](/wiki/Skyrim:Amulet_of_Mara "Skyrim:Amulet of Mara") |  | ☒ |  |
| [Viriya](/wiki/Skyrim:Viriya "Skyrim:Viriya")[CC](/wiki/Skyrim:Fishing "Skyrim:Fishing") | Marketplace Stall | Crab-based items | **150** | ☒ | ☑ |
| [Madesi](/wiki/Skyrim:Madesi "Skyrim:Madesi") | Marketplace Stall | Jeweler | **750** | ☒(☑[†](#intnote_Brand-SheiGrelkaMadesiMarise)) |  |
| [Marise Aravel](/wiki/Skyrim:Marise_Aravel "Skyrim:Marise Aravel") | Marketplace Stall | General | **50** | ☒(☑[†](#intnote_Brand-SheiGrelkaMadesiMarise)) |  |
| [Syndus](/wiki/Skyrim:Syndus "Skyrim:Syndus") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Blacksmith | **1000** | ☒ | ☑ |
| [Tonilia](/wiki/Skyrim:Tonilia "Skyrim:Tonilia") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Fence | **1000**-**4000** | ☒ | ☑ |
| [Vanryth Gatharian](/wiki/Skyrim:Vanryth_Gatharian "Skyrim:Vanryth Gatharian") | [The Ragged Flagon](/wiki/Skyrim:The_Ragged_Flagon "Skyrim:The Ragged Flagon") | Blacksmith | **1000** | ☒ | ☑ |
| [Wylandriah](/wiki/Skyrim:Wylandriah "Skyrim:Wylandriah") | in [Mistveil Keep](/wiki/Skyrim:Mistveil_Keep "Skyrim:Mistveil Keep") | Spells | **1000** | ☑ | ☑ |

- Galathil won't change your face if you are a [vampire](/wiki/Skyrim:Vampirism "Skyrim:Vampirism") or a [Vampire Lord](/wiki/Skyrim:Vampire_Lord "Skyrim:Vampire Lord")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard").
- Viriya's stall becomes available once [End of the Line](/wiki/Skyrim:End_of_the_Line "Skyrim:End of the Line")[CC](/wiki/Skyrim:Fishing "Skyrim:Fishing") is finished.
- Tonilia sometimes has the "What'll you give me for these?" dialogue option, and other times has the "What have you got for sale?" dialogue option.
- Syndus, Herluin Lothaire, Arnskar Ember-Master, and Vanryth Gatharian are added to the Ragged Flagon (in that order) during [Under New Management](/wiki/Skyrim:Under_New_Management "Skyrim:Under New Management").
- All merchants in the Ragged Flagon are part of the ThievesGuildFaction, and will jump to the Guild's defense if hostilities erupt down there.

[†](#note_GrelkaBrand-SheiMadesiMarise)Version 2.1.3 of the [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch") makes it possible to invest with Brand-Shei, Grelka, Madesi, and Marise.

[‡](#note_GrelkaBrand-SheiMadesiMarise)Be warned, however, that version 3.0.1 of the [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch") reverses that, and they cannot be invested with anymore.

#### Bugs

- Despite being a fence, there is a chance that Tonilia may eventually stop accepting stolen goods.
  - The [Official Skyrim Patch](/wiki/Skyrim:Patch "Skyrim:Patch"), version 1.4, fixes this bug.
- If you turn Romlyn in to [Indaryn](/wiki/Skyrim:Indaryn "Skyrim:Indaryn") during [Under the Table](/wiki/Skyrim:Under_the_Table "Skyrim:Under the Table"), he will keep working at the meadery and continue to sell his under-the-table Black-Briar Mead, despite saying *"A Dreth never forgets a traitor."* each time you talk to him.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.4, addresses this issue. Romlyn will be jailed if you turn him in and he will no longer offer to sell you any mead.
- Helping Shadr will allow you to ride the horses at Riften Stables for free, due to him being in the same ownership faction as the stablemaster. The problem is that horses cost 1,000 gold, making them way too valuable to let stablemasters let you ride them for free after completing a small favor.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.1.2, addresses this issue. ([details](https://afktrack.afkmods.com/index.php?a=issues&i=19062)) The ownership of the horses was changed to just Hofgrir, rather than the faction, preventing this issue.

### Other Locations

| Merchant Name | Store Place | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Filnjar](/wiki/Skyrim:Filnjar "Skyrim:Filnjar") | [Filnjar's House](/wiki/Skyrim:Filnjar%27s_House "Skyrim:Filnjar's House") | [Shor's Stone](/wiki/Skyrim:Shor%27s_Stone "Skyrim:Shor's Stone") | Blacksmith | **500** | ☒(☑) | ☑ |  |
| [Grosta](/wiki/Skyrim:Grosta "Skyrim:Grosta") |  | [Heartwood Mill](/wiki/Skyrim:Heartwood_Mill "Skyrim:Heartwood Mill") | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |  |
| [Wilhelm](/wiki/Skyrim:Wilhelm "Skyrim:Wilhelm") ([Lynly Star-Sung](/wiki/Skyrim:Lynly_Star-Sung "Skyrim:Lynly Star-Sung")) | [Vilemyr Inn](/wiki/Skyrim:Vilemyr_Inn "Skyrim:Vilemyr Inn") | [Ivarstead](/wiki/Skyrim:Ivarstead "Skyrim:Ivarstead") | Innkeeper | **100** | ☒ |  |  |
| [Dealer](/wiki/Skyrim:Dealer "Skyrim:Dealer")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Redwater Den](/wiki/Skyrim:Redwater_Den "Skyrim:Redwater Den")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Innkeeper (also sells [Redwater Skooma](/wiki/Skyrim:Redwater_Skooma "Skyrim:Redwater Skooma")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard")) | **100** | ☒ |  | Hostile if you attempt to halt the Redwater Skooma operation |
| [Florentius Baenius](/wiki/Skyrim:Florentius_Baenius "Skyrim:Florentius Baenius")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Apothecary, Spells | **500** | ☑ | ☑ | Hostile to vampires |
| [Gunmar](/wiki/Skyrim:Gunmar "Skyrim:Gunmar")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Blacksmith | **1000** |  | ☑ | Hostile to vampires |
| [Sorine Jurard](/wiki/Skyrim:Sorine_Jurard "Skyrim:Sorine Jurard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") |  | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | General | **750** |  | ☑ | Hostile to vampires |

- Filnjar in Shor's Stone can be invested, with the most recent versions of Skyrim and the Unofficial Skyrim Special Edition Patch (please check if he can be invested with the Legendary version, or without the Unofficial Patches at all)

#### Bugs

- [Atub](/wiki/Skyrim:Atub "Skyrim:Atub") and [Garakh](/wiki/Skyrim:Garakh "Skyrim:Garakh") at [Largashbur](/wiki/Skyrim:Largashbur "Skyrim:Largashbur") were apparently intended to be merchants (apothecary and blacksmith respectively), but do not function as merchants themselves.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.5, addresses this issue. They were assigned the wrong settings. Once fixed, they will be affected by [Master Trader](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader"), but not [Investor](/wiki/Skyrim:Investor "Skyrim:Investor").

### Raven Rock

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Fethis Alor](/wiki/Skyrim:Fethis_Alor "Skyrim:Fethis Alor") | [Alor House](/wiki/Skyrim:Alor_House "Skyrim:Alor House") | General | **1500** |  | ☑ |  |
| [Garyn Ienth](/wiki/Skyrim:Garyn_Ienth "Skyrim:Garyn Ienth") | [Ienth Farm](/wiki/Skyrim:Ienth_Farm "Skyrim:Ienth Farm") | Innkeeper | **50** | ☒ |  |  |
| [Geldis Sadri](/wiki/Skyrim:Geldis_Sadri "Skyrim:Geldis Sadri") | [The Retching Netch](/wiki/Skyrim:The_Retching_Netch "Skyrim:The Retching Netch") | Innkeeper | **100** | ☒ |  |  |
| [Glover Mallory](/wiki/Skyrim:Glover_Mallory "Skyrim:Glover Mallory") | [Glover Mallory's House](/wiki/Skyrim:Glover_Mallory%27s_House "Skyrim:Glover Mallory's House") | Blacksmith | **2000** | ☑ | ☑ |  |
| [Milore Ienth](/wiki/Skyrim:Milore_Ienth "Skyrim:Milore Ienth") | [Ienth Farm](/wiki/Skyrim:Ienth_Farm "Skyrim:Ienth Farm") | Apothecary | **1000** |  | ☑ |  |

### Tel Mithryn

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Elynea Mothren](/wiki/Skyrim:Elynea_Mothren "Skyrim:Elynea Mothren") | [Tel Mithryn Apothecary](/wiki/Skyrim:Tel_Mithryn_Apothecary "Skyrim:Tel Mithryn Apothecary") | Apothecary | **1000** |  | ☑ |  |
| [Neloth](/wiki/Skyrim:Neloth "Skyrim:Neloth") | [Tel Mithryn](/wiki/Skyrim:Tel_Mithryn_(tower) "Skyrim:Tel Mithryn (tower)") | Staves & Spells | **1000** |  | ☑ |  |
| [Talvas Fathryon](/wiki/Skyrim:Talvas_Fathryon "Skyrim:Talvas Fathryon") | [Tel Mithryn](/wiki/Skyrim:Tel_Mithryn_(tower) "Skyrim:Tel Mithryn (tower)") | Spells | **500** |  | ☑ |  |
| [Revus Sarvani](/wiki/Skyrim:Revus_Sarvani "Skyrim:Revus Sarvani") | [Tel Mithryn](/wiki/Skyrim:Tel_Mithryn_(tower) "Skyrim:Tel Mithryn (tower)") | General | **500** | ☒ |  | Found on outskirts of the town with his silt strider |

### Others

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Edla](/wiki/Skyrim:Edla "Skyrim:Edla") | [Edla's House](/wiki/Skyrim:Edla%27s_House "Skyrim:Edla's House") in [Skaal Village](/wiki/Skyrim:Skaal_Village "Skyrim:Skaal Village") | Apothecary | **50** | ☒ |  |  |
| [Baldor Iron-Shaper](/wiki/Skyrim:Baldor_Iron-Shaper "Skyrim:Baldor Iron-Shaper") | [Baldor Iron-Shaper's House](/wiki/Skyrim:Baldor_Iron-Shaper%27s_House "Skyrim:Baldor Iron-Shaper's House") in [Skaal Village](/wiki/Skyrim:Skaal_Village "Skyrim:Skaal Village") | Blacksmith | **1000** |  | ☑ |  |
| [Blacksmith](/wiki/Skyrim:Blacksmith_(NPC) "Skyrim:Blacksmith (NPC)")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | [Ashfall's Tear](/wiki/Skyrim:Ashfall%27s_Tear "Skyrim:Ashfall's Tear")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | Blacksmith | **2130** | [(?)](/wiki/Category:Pages_Missing_Data "Category:Pages Missing Data") | ☑ | Only appears if you side with the [Tribunal Temple](/wiki/Skyrim:Tribunal_Temple "Skyrim:Tribunal Temple") during [Her Word Against Theirs](/wiki/Skyrim:Her_Word_Against_Theirs "Skyrim:Her Word Against Theirs") |
| [Caretaker Ineril](/wiki/Skyrim:Caretaker_Ineril "Skyrim:Caretaker Ineril")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | [Ashfall's Tear](/wiki/Skyrim:Ashfall%27s_Tear "Skyrim:Ashfall's Tear")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | General | **1500** | [(?)](/wiki/Category:Pages_Missing_Data "Category:Pages Missing Data") | ☑ | Only appears after you give one of the translated [Propaganda Letters](/wiki/Skyrim:Propaganda_Letter "Skyrim:Propaganda Letter") to [Geldis Sadri](/wiki/Skyrim:Geldis_Sadri "Skyrim:Geldis Sadri") during [Her Word Against Theirs](/wiki/Skyrim:Her_Word_Against_Theirs "Skyrim:Her Word Against Theirs") |
| [Curate Melita](/wiki/Skyrim:Curate_Melita "Skyrim:Curate Melita")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | [Ashfall's Tear](/wiki/Skyrim:Ashfall%27s_Tear "Skyrim:Ashfall's Tear")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | Apothecary | **2000** | [(?)](/wiki/Category:Pages_Missing_Data "Category:Pages Missing Data") | ☑ | Only available if you set her free during [Careless Curation](/wiki/Skyrim:Careless_Curation "Skyrim:Careless Curation") |
| [Priest Drureth](/wiki/Skyrim:Priest_Drureth "Skyrim:Priest Drureth")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | [Ashfall's Tear](/wiki/Skyrim:Ashfall%27s_Tear "Skyrim:Ashfall's Tear")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") | Apothecary | **2000** | [(?)](/wiki/Category:Pages_Missing_Data "Category:Pages Missing Data") | ☑ |  |
| [Falas Selvayn](/wiki/Skyrim:Falas_Selvayn "Skyrim:Falas Selvayn") | [Ramshackle Trading Post](/wiki/Skyrim:Ramshackle_Trading_Post "Skyrim:Ramshackle Trading Post") | General | **750** | ☒ | ☑ | Only appears if you visit the trading post at night |
| [Halbarn Iron-Fur](/wiki/Skyrim:Halbarn_Iron-Fur "Skyrim:Halbarn Iron-Fur") | [Bujold's Retreat](/wiki/Skyrim:Bujold%27s_Retreat "Skyrim:Bujold's Retreat") /  [Thirsk Mead Hall](/wiki/Skyrim:Thirsk_Mead_Hall "Skyrim:Thirsk Mead Hall") | Blacksmith | **1000** |  | ☑ | Only available at Thirsk Mead Hall if you finish [Retaking Thirsk](/wiki/Skyrim:Retaking_Thirsk "Skyrim:Retaking Thirsk") |
| [Elmus](/wiki/Skyrim:Elmus "Skyrim:Elmus") | [Bujold's Retreat](/wiki/Skyrim:Bujold%27s_Retreat "Skyrim:Bujold's Retreat") / [Thirsk Mead Hall](/wiki/Skyrim:Thirsk_Mead_Hall "Skyrim:Thirsk Mead Hall") | Food and Drink | **100** | ☒ | ☑ | Only available at Thirsk Mead Hall if you finish [Retaking Thirsk](/wiki/Skyrim:Retaking_Thirsk "Skyrim:Retaking Thirsk") |
| [Ancarion](/wiki/Skyrim:Ancarion "Skyrim:Ancarion") | [Northshore Landing](/wiki/Skyrim:Northshore_Landing "Skyrim:Northshore Landing") | Stalhrim equipment | **1000** | ☒ | ☒ (☑)[†](#intnote_Ancarion) | Only available if you successfully negotiate with him during [A New Source of Stalhrim](/wiki/Skyrim:A_New_Source_of_Stalhrim "Skyrim:A New Source of Stalhrim") |
| [Majni](/wiki/Skyrim:Majni "Skyrim:Majni") | [Frostmoon Crag](/wiki/Skyrim:Frostmoon_Crag "Skyrim:Frostmoon Crag") | General, Werewolf rings | **25**-**125** |  |  | Only available at the camp if you are a werewolf |

- If you want to convince Ancarion to let you sell Stalhrim equipment to him, your [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") skill must be 75 or better.

[†](#note_Ancarion)Ancarion's shop benefits from the Master Trader perk with version 2.0.3 of the [Unofficial Dragonborn Patch](/wiki/Skyrim_Mod:Unofficial_Dragonborn_Patch "Skyrim Mod:Unofficial Dragonborn Patch").

#### Bugs

- Despite being a blacksmith, Baldor Iron-Shaper is incorrectly configured to buy any type of item regardless if you have the Merchant perk active or not.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Dragonborn Patch](/wiki/Skyrim_Mod:Unofficial_Dragonborn_Patch "Skyrim Mod:Unofficial Dragonborn Patch"), version 2.0.8, addresses this issue. You now need to have the Merchant perk active to sell him anything else.
- Some merchants on Solstheim can incorrectly prompt you with dialogue that's used by Fences. There are no Fences on the island, unless you invest in Glover with the Fence perk active.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Dragonborn Patch](/wiki/Skyrim_Mod:Unofficial_Dragonborn_Patch "Skyrim Mod:Unofficial Dragonborn Patch"), version 2.0.8, fixes this bug.

### Riverwood

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Alvor](/wiki/Skyrim:Alvor "Skyrim:Alvor") | [Alvor and Sigrid's House](/wiki/Skyrim:Alvor_and_Sigrid%27s_House "Skyrim:Alvor and Sigrid's House") | Blacksmith | **500** | ☑ | ☑ |
| [Hod](/wiki/Skyrim:Hod "Skyrim:Hod") | Riverwood sawmill | [Lumber](/wiki/Skyrim:Sawn_Log "Skyrim:Sawn Log")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") |  | ☒ |  |
| [Orgnar](/wiki/Skyrim:Orgnar "Skyrim:Orgnar") | [Sleeping Giant Inn](/wiki/Skyrim:Sleeping_Giant_Inn "Skyrim:Sleeping Giant Inn") | Innkeeper (also sells [Ingredients](/wiki/Skyrim:Ingredients "Skyrim:Ingredients")) | **100** | ☒ |  |
| [Lucan Valerius](/wiki/Skyrim:Lucan_Valerius "Skyrim:Lucan Valerius") ([Camilla Valerius](/wiki/Skyrim:Camilla_Valerius "Skyrim:Camilla Valerius")) | [Riverwood Trader](/wiki/Skyrim:Riverwood_Trader "Skyrim:Riverwood Trader") | General; sells [Blue Mage Robes](/wiki/Skyrim:Blue_Mage_Robes "Skyrim:Blue Mage Robes"), several Spell Tomes | **750** | ☑ | ☑ |

- If you place items in the cupboard behind Lucan's counter, they will show up in his inventory. Purchasing stolen items you place in there will remove their stolen tags. Don't put torches in there, though, as they won't add to what Lucan has for sale.

### Bugs

- If you invest 500 gold into the Riverwood Trader (using the [Investor](/wiki/Skyrim:Investor "Skyrim:Investor") perk), regardless of if it's operated by Lucan or Camilla, it adds 10,000 gold instead of 500 gold to their inventory.
  - The [Official Skyrim Patch](/wiki/Skyrim:Patch "Skyrim:Patch"), version 1.9, fixes this bug.

### Whiterun

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Adrianne Avenicci](/wiki/Skyrim:Adrianne_Avenicci "Skyrim:Adrianne Avenicci") (Outside) | [Warmaiden's](/wiki/Skyrim:Warmaiden%27s "Skyrim:Warmaiden's") | Blacksmith | **1000** | ☑ | ☑ |
| [Adrianne Avenicci](/wiki/Skyrim:Adrianne_Avenicci "Skyrim:Adrianne Avenicci"); [Ulfberth War-Bear](/wiki/Skyrim:Ulfberth_War-Bear "Skyrim:Ulfberth War-Bear") | [Warmaiden's](/wiki/Skyrim:Warmaiden%27s "Skyrim:Warmaiden's") | Blacksmith | **1000** | ☑ | ☑ |
| [Anoriath](/wiki/Skyrim:Anoriath "Skyrim:Anoriath") | Marketplace Stall | Innkeeper | **50** | ☒(☑) | ☑ |
| [Arcadia](/wiki/Skyrim:Arcadia "Skyrim:Arcadia") | [Arcadia's Cauldron](/wiki/Skyrim:Arcadia%27s_Cauldron "Skyrim:Arcadia's Cauldron") | Apothecary | **500** | ☑ | ☑ |
| [Belethor](/wiki/Skyrim:Belethor "Skyrim:Belethor") | [Belethor's General Goods](/wiki/Skyrim:Belethor%27s_General_Goods "Skyrim:Belethor's General Goods") | General | **750** | ☑ | ☑ |
| [Carlotta Valentia](/wiki/Skyrim:Carlotta_Valentia "Skyrim:Carlotta Valentia") | Marketplace Stall | Innkeeper | **50** | ☒ | ☑ |
| [Elrindir](/wiki/Skyrim:Elrindir "Skyrim:Elrindir") | [The Drunken Huntsman](/wiki/Skyrim:The_Drunken_Huntsman "Skyrim:The Drunken Huntsman") | [Armor](/wiki/Skyrim:Armor "Skyrim:Armor"), [Arrows](/wiki/Skyrim:Arrows "Skyrim:Arrows"), [Food](/wiki/Skyrim:Food "Skyrim:Food"), [Tools](/wiki/Skyrim:Tools "Skyrim:Tools"), [Weapons](/wiki/Skyrim:Weapons "Skyrim:Weapons") | **750** | ☒(☑) | ☑ |
| [Eorlund Gray-Mane](/wiki/Skyrim:Eorlund_Gray-Mane "Skyrim:Eorlund Gray-Mane") | [Skyforge](/wiki/Skyrim:Skyforge "Skyrim:Skyforge") | Blacksmith | **1000**-**2500** |  | ☑ |
| [Farengar Secret-Fire](/wiki/Skyrim:Farengar_Secret-Fire "Skyrim:Farengar Secret-Fire") | [Dragonsreach](/wiki/Skyrim:Dragonsreach "Skyrim:Dragonsreach") | Spells | **500** | ☑ | ☑ |
| [Fralia Gray-Mane](/wiki/Skyrim:Fralia_Gray-Mane "Skyrim:Fralia Gray-Mane") | Marketplace Stall | Jeweler | **50** | ☒ | ☒ |
| [Hulda](/wiki/Skyrim:Hulda "Skyrim:Hulda"); [Saadia](/wiki/Skyrim:Saadia "Skyrim:Saadia") ([Ysolda](/wiki/Skyrim:Ysolda "Skyrim:Ysolda")) | [The Bannered Mare](/wiki/Skyrim:The_Bannered_Mare "Skyrim:The Bannered Mare") | Innkeeper | **100** | ☒ | ☑ |
| [Mallus Maccius](/wiki/Skyrim:Mallus_Maccius "Skyrim:Mallus Maccius") | [Honningbrew Meadery](/wiki/Skyrim:Honningbrew_Meadery "Skyrim:Honningbrew Meadery") | Fence | **1000**-**4000** | ☒ | ☑ |
| [Sabjorn](/wiki/Skyrim:Sabjorn "Skyrim:Sabjorn") | [Honningbrew Meadery](/wiki/Skyrim:Honningbrew_Meadery "Skyrim:Honningbrew Meadery") | Innkeeper | **100** | ☒ |  |
| [Skulvar Sable-Hilt](/wiki/Skyrim:Skulvar_Sable-Hilt "Skyrim:Skulvar Sable-Hilt") ([Jervar](/wiki/Skyrim:Jervar "Skyrim:Jervar")) | [Whiterun Stables](/wiki/Skyrim:Whiterun_Stables "Skyrim:Whiterun Stables") | [Horses](/wiki/Skyrim:Horses "Skyrim:Horses") |  | ☒ |  |

- If something happens to Belethor, it's possible for Ysolda to inherit Belethor's General Goods. The reason for this is unknown.
- Despite the fact that [Olfina Gray-Mane](/wiki/Skyrim:Olfina_Gray-Mane "Skyrim:Olfina Gray-Mane") is part of the "food vendor" class, she isn't actually a food merchant herself.
- Adrianne Avenicci is unique in having access to two merchant chests; when she is outside during the day, she sells items from a separate chest. When she is inside and the store is open, she uses the same chest as Ulfberth War-Bear. The two chests are counted as separate stores for the purpose of investing. However, you can only invest once.

#### Bugs

- Adrianne Avenicci, Arcadia, Belethor, and Ulfberth War-Bear may have [Do Not Delete](/wiki/Skyrim:Do_Not_Delete "Skyrim:Do Not Delete") chests for sale.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.4, fixes this bug. ([details](https://afktrack.afkmods.com/index.php?a=issues&i=8125))
- Anoriath will allow you to invest in his store, but his available gold will not increase due to a [bug](/wiki/Skyrim:Anoriath#Bugs "Skyrim:Anoriath").
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.4, fixes this bug.
- Anoriath owns Fralia Gray-Mane's merchant chest when it doesn't belong to him.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.4, fixes this bug.
- Due to dialogue condition errors, you cannot invest in The Drunken Huntsman by talking to Elrindir.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.6, fixes this bug.

### Other Locations

| Merchant Name | Store Name | Town | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- | --- |
| [Mralki](/wiki/Skyrim:Mralki "Skyrim:Mralki") | [Frostfruit Inn](/wiki/Skyrim:Frostfruit_Inn "Skyrim:Frostfruit Inn") | [Rorikstead](/wiki/Skyrim:Rorikstead "Skyrim:Rorikstead") | Innkeeper | **100** | ☒ |  |

### Winterhold

| Merchant Name | Store Name | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Birna](/wiki/Skyrim:Birna "Skyrim:Birna") | [Birna's Oddments](/wiki/Skyrim:Birna%27s_Oddments "Skyrim:Birna's Oddments") | General | **750** | ☑ | ☑ |
| [Dagur](/wiki/Skyrim:Dagur "Skyrim:Dagur"); [Haran](/wiki/Skyrim:Haran "Skyrim:Haran") | [The Frozen Hearth](/wiki/Skyrim:The_Frozen_Hearth "Skyrim:The Frozen Hearth") | Innkeeper | **100** | ☒ | ☑ |
| [Nelacar](/wiki/Skyrim:Nelacar "Skyrim:Nelacar") | [The Frozen Hearth](/wiki/Skyrim:The_Frozen_Hearth "Skyrim:The Frozen Hearth") | Spells | **500** |  | ☑ |

### College of Winterhold

| Merchant Name | Store Location | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Colette Marence](/wiki/Skyrim:Colette_Marence "Skyrim:Colette Marence") | [Hall of Countenance](/wiki/Skyrim:Hall_of_Countenance "Skyrim:Hall of Countenance") | Spells ([Restoration](/wiki/Skyrim:Restoration "Skyrim:Restoration")) | **500** |  | ☑ |  |
| [Drevis Neloren](/wiki/Skyrim:Drevis_Neloren "Skyrim:Drevis Neloren") | [Hall of Countenance](/wiki/Skyrim:Hall_of_Countenance "Skyrim:Hall of Countenance") | Spells ([Illusion](/wiki/Skyrim:Illusion "Skyrim:Illusion")) | **500** |  | ☑ |  |
| [Enthir](/wiki/Skyrim:Enthir "Skyrim:Enthir") | [Hall of Attainment](/wiki/Skyrim:Hall_of_Attainment "Skyrim:Hall of Attainment") | General | **500** | ☒ | ☑ | Stocks a [Black Soul Gem](/wiki/Skyrim:Black_Soul_Gem "Skyrim:Black Soul Gem") and 2 [Daedra Hearts](/wiki/Skyrim:Daedra_Heart "Skyrim:Daedra Heart") |
| Fence | **1000**-**4000** |  |
| [Faralda](/wiki/Skyrim:Faralda "Skyrim:Faralda") | [Hall of Countenance](/wiki/Skyrim:Hall_of_Countenance "Skyrim:Hall of Countenance") | Spells ([Destruction](/wiki/Skyrim:Destruction "Skyrim:Destruction")) | **500** |  | ☑ |  |
| [Phinis Gestor](/wiki/Skyrim:Phinis_Gestor "Skyrim:Phinis Gestor") | [Hall of Countenance](/wiki/Skyrim:Hall_of_Countenance "Skyrim:Hall of Countenance") | Spells ([Conjuration](/wiki/Skyrim:Conjuration "Skyrim:Conjuration")) | **500** |  | ☑ |  |
| [Tolfdir](/wiki/Skyrim:Tolfdir "Skyrim:Tolfdir") | [Hall of Attainment](/wiki/Skyrim:Hall_of_Attainment "Skyrim:Hall of Attainment") | Spells ([Alteration](/wiki/Skyrim:Alteration "Skyrim:Alteration")) | **500** |  | ☑ |  |
| [Urag gro-Shub](/wiki/Skyrim:Urag_gro-Shub "Skyrim:Urag gro-Shub") | [The Arcanaeum](/wiki/Skyrim:The_Arcanaeum "Skyrim:The Arcanaeum") | [Books](/wiki/Skyrim:Books "Skyrim:Books") | **500** |  | ☑ |  |

#### Bugs

- Enthir may only be available as a fence when he isn't in the Hall of Attainment.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.2, addresses this issue. Enthir will now be available for fencing at all times once his fence setup quest is finished.
- After completing the Thieves Guild quests and joining the College, Enthir may lose his status as a fence. Despite having two separate dialogue options (one for his old retail mode and another for his fence mode), he will only buy non-stolen goods, and will be limited to the original 500 gold.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.3, fixes this bug.
- Urag gro-Shub has no scrolls in his vendor inventory despite clearly stating he sells them when asked about it.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.4, fixes this bug.
- Version 4.2.4 of the Unofficial Skyrim Special Edition Patch overlooked a major detail. Urag-gro Shub does not offer the scrolls given to him because the VendorItemScroll keyword was never added to his custom vendor formlist.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.5, fixes this bug.

### Khajiit Traders

| Merchant Name | Store Location | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") |
| --- | --- | --- | --- | --- | --- |
| [Ahkari](/wiki/Skyrim:Ahkari "Skyrim:Ahkari") | [Dawnstar](/wiki/Skyrim:Dawnstar "Skyrim:Dawnstar") or [Riften](/wiki/Skyrim:Riften "Skyrim:Riften") | General; Sells [Moon Sugar](/wiki/Skyrim:Moon_Sugar "Skyrim:Moon Sugar") and [Skooma](/wiki/Skyrim:Skooma "Skyrim:Skooma") | **750** | ☑ | ☑ |
| [Atahbah](/wiki/Skyrim:Atahbah "Skyrim:Atahbah") | [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth") or [Whiterun](/wiki/Skyrim:Whiterun "Skyrim:Whiterun") | [Fence](/wiki/Skyrim:Fence_(merchant) "Skyrim:Fence (merchant)") | **1000**-**4000** | ☒ | ☑ |
| [Ma'dran](/wiki/Skyrim:Ma%27dran "Skyrim:Ma'dran") | [Solitude](/wiki/Skyrim:Solitude "Skyrim:Solitude") or [Windhelm](/wiki/Skyrim:Windhelm "Skyrim:Windhelm") | General; Sells [Moon Sugar](/wiki/Skyrim:Moon_Sugar "Skyrim:Moon Sugar") and [Skooma](/wiki/Skyrim:Skooma "Skyrim:Skooma") | **750** | ☑ | ☑ |
| [Ma'jhad](/wiki/Skyrim:Ma%27jhad "Skyrim:Ma'jhad") | [Solitude](/wiki/Skyrim:Solitude "Skyrim:Solitude") or [Windhelm](/wiki/Skyrim:Windhelm "Skyrim:Windhelm") | [Fence](/wiki/Skyrim:Fence_(merchant) "Skyrim:Fence (merchant)") | **1000**-**4000** | ☒ | ☑ |
| [Ri'saad](/wiki/Skyrim:Ri%27saad "Skyrim:Ri'saad") | [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth") or [Whiterun](/wiki/Skyrim:Whiterun "Skyrim:Whiterun") | General; Sells [Moon Sugar](/wiki/Skyrim:Moon_Sugar "Skyrim:Moon Sugar") and [Skooma](/wiki/Skyrim:Skooma "Skyrim:Skooma") | **750** | ☑ | ☑ |
| [Zaynabi](/wiki/Skyrim:Zaynabi "Skyrim:Zaynabi") | [Dawnstar](/wiki/Skyrim:Dawnstar "Skyrim:Dawnstar") or [Riften](/wiki/Skyrim:Riften "Skyrim:Riften") | [Fence](/wiki/Skyrim:Fence_(merchant) "Skyrim:Fence (merchant)") | **1000**-**4000** | ☒ | ☑ |

### Other

| Merchant Name | Store Location | Merchandise | Gold | [Invest](/wiki/Skyrim:Investor "Skyrim:Investor") | [Master](/wiki/Skyrim:Master_Trader "Skyrim:Master Trader") | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Imperial Quartermaster](/wiki/Skyrim:Imperial_Quartermaster "Skyrim:Imperial Quartermaster") | Most [Imperial](/wiki/Skyrim:Imperial "Skyrim:Imperial") [camps](/wiki/Skyrim:Military_Camps "Skyrim:Military Camps") | Blacksmith | **1000** | ☒ | ☒ | Hostile if you have [joined the Stormcloaks](/wiki/Skyrim:Joining_the_Stormcloaks "Skyrim:Joining the Stormcloaks") |
| [Stormcloak Quartermaster](/wiki/Skyrim:Stormcloak_Quartermaster "Skyrim:Stormcloak Quartermaster") | Most [Stormcloak](/wiki/Skyrim:Stormcloaks "Skyrim:Stormcloaks") [camps](/wiki/Skyrim:Military_Camps "Skyrim:Military Camps") | Blacksmith | **1000** | ☒ | ☒ | Hostile if you have [joined the Imperials](/wiki/Skyrim:Joining_the_Legion "Skyrim:Joining the Legion") |
| [Hunter](/wiki/Skyrim:Hunter "Skyrim:Hunter") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness; some [unmarked places](/wiki/Skyrim:Unmarked_Places "Skyrim:Unmarked Places") | Meat, Hides | **3**-**36**[\*](#intnote_Hunters) | ☒ | ☒ | May occasionally have a [dog](/wiki/Skyrim:Dog "Skyrim:Dog") present with them |
| [Hunter](/wiki/Skyrim:Hunter "Skyrim:Hunter")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness | Meat, Hides | **3**-**36**[\*](#intnote_Hunters) | ☒ | ☒ | This hunter may be infected with [Sanginare Vampiris](/wiki/Skyrim:Sanguinare_Vampiris "Skyrim:Sanguinare Vampiris"); if so, you must give him a [Cure Disease](/wiki/Skyrim:Cure_Disease "Skyrim:Cure Disease") potion to be able to trade with him once again. You'll also gain 100 gold and the location of a vampire lair as a reward. Only a found or purchased potion will work; one created using [Alchemy](/wiki/Skyrim:Alchemy "Skyrim:Alchemy") won't. If you cannot, the hunter will flee in terror. |
| [Orc Hunter](/wiki/Skyrim:Orc_Hunter "Skyrim:Orc Hunter") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness | Meat, Hides | **10**-**50** | ☒ | ☒ | May be hostile towards each other (or you) or have nothing for sale |
| [Peddler](/wiki/Skyrim:Peddler "Skyrim:Peddler") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness (being attacked by [bandits](/wiki/Skyrim:Bandit "Skyrim:Bandit") or [Forsworn](/wiki/Skyrim:Forsworn "Skyrim:Forsworn")) | General Goods | **50**-**77** | ☒ | ☒ | May sometimes appear dead by the time of your arrival |
| [Skooma Dealer](/wiki/Skyrim:Skooma_Dealer_(NPC) "Skyrim:Skooma Dealer (NPC)") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness | [Moon Sugar](/wiki/Skyrim:Moon_Sugar "Skyrim:Moon Sugar"), [Skooma](/wiki/Skyrim:Skooma "Skyrim:Skooma"), [Sleeping Tree Sap](/wiki/Skyrim:Sleeping_Tree_Sap "Skyrim:Sleeping Tree Sap") | **20**-**56** | ☒ | ☒ | Hostile if you fail to intimidate them or if you tell them what they're doing is illegal |
| [Sond](/wiki/Skyrim:Sond_(child) "Skyrim:Sond (child)") | [Randomly anywhere](/wiki/Skyrim:World_Interactions "Skyrim:World Interactions") in the wilderness | Miscellaneous Dwemer equipment | **20** | ☒ | ☒ | Will add [Deep Folk Crossing](/wiki/Skyrim:Deep_Folk_Crossing "Skyrim:Deep Folk Crossing") to your map for 1 gold |
| [Spouses](/wiki/Skyrim:Marriage "Skyrim:Marriage") | Wherever you and your spouse live | General by default[†](#intnote_Marriage) | **100**-**1000** | unknown | unknown | Will give you a cumulative 100 gold a day or more |
| [Personal Stewards](/wiki/Skyrim:Personal_Steward "Skyrim:Personal Steward")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") | Wherever your [player-built home](/wiki/Skyrim:Construction "Skyrim:Construction")[HF](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") is | Improvements to your property[†](#intnote_PersonalSteward) |  |  |  | Can also be assigned to [Goldenhills Plantation](/wiki/Skyrim:Goldenhills_Plantation "Skyrim:Goldenhills Plantation")[CC](/wiki/Skyrim:Farming "Skyrim:Farming") |
| [Morven Stroud](/wiki/Skyrim:Morven_Stroud "Skyrim:Morven Stroud")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Soul Cairn](/wiki/Skyrim:Soul_Cairn "Skyrim:Soul Cairn")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | Swords, Battleaxes, Armor, Spell Tomes | **N/A** | ☒ | ☒ | Weapons and armor may be [enchanted](/wiki/Skyrim:Enchanting "Skyrim:Enchanting"); may offer Expert-level [Spell Tomes](/wiki/Skyrim:Spell_Tomes "Skyrim:Spell Tomes")[†](#intnote_MorvenStroud) |
| [Dremora Merchant](/wiki/Skyrim:Dremora_Merchant "Skyrim:Dremora Merchant")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | Summoned to your location | [Heavy armor](/wiki/Skyrim:Heavy_Armor "Skyrim:Heavy Armor"), [Weapons](/wiki/Skyrim:Weapons "Skyrim:Weapons") | **2000** | ☒ | ☒ | Items are [enchanted](/wiki/Skyrim:Enchanting "Skyrim:Enchanting"); may sell [Dragon items](/wiki/Skyrim:Dragon_Items "Skyrim:Dragon Items")[†](#intnote_DremoraMerchant) |

[\*](#note_Hunters)Hunters will not dissipate their wealth when you sell them things. They have theoretically unlimited wealth. It is just that they will only pay up to a certain amount of gold for a single item, or a single stack of items.

[†](#note_Marriage)The merchandise your spouse sells depends on whether or not he or she was a merchant beforehand. If so, it will reflect on what type of merchandise they originally sold. If not, they will sell general merchandise.

[†](#note_PersonalSteward)The available improvements your Personal Steward sells at Goldenhills Plantation are different from the ones available at your player-built houses.

[†](#note_MorvenStroud)Morven Stroud will tell you that gold isn't valuable in the Soul Cairn. Instead, he will give you a random item of your choosing for 25 [soul husks](/wiki/Skyrim:Soul_Husk "Skyrim:Soul Husk") apiece. You can get up to Expert-level Spell Tomes from him, whether you know their spells or not.

[†](#note_DremoraMerchant)Choosing the [Black Market](/wiki/Skyrim:Black_Market "Skyrim:Black Market") power at the end of the [Black Book: Untold Legends](/wiki/Skyrim:Black_Book:_Untold_Legends_(quest) "Skyrim:Black Book: Untold Legends (quest)")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") quest makes the [Dremora Merchant](/wiki/Skyrim:Dremora_Merchant "Skyrim:Dremora Merchant") available. You can then summon him to your location, regardless of whether you are in Solstheim or Skyrim.

## Merchant Trainers

You can ask these merchants for training.

[![Common](//images.uesp.net/e/ef/SR-icon-Basic_Trainer.png)](/wiki/File:SR-icon-Basic_Trainer.png "Common") - Common (0-50), [![Expert](//images.uesp.net/c/c7/SR-icon-Advanced_Trainer.png)](/wiki/File:SR-icon-Advanced_Trainer.png "Expert") - Expert (0-75), [![Master](//images.uesp.net/5/53/SR-icon-Master_Trainer.png)](/wiki/File:SR-icon-Master_Trainer.png "Master") - Master (0-90)

| Merchant Name | Store Location | Skill |
| --- | --- | --- |
| [Arcadia](/wiki/Skyrim:Arcadia "Skyrim:Arcadia") | [Arcadia's Cauldron](/wiki/Skyrim:Arcadia%27s_Cauldron "Skyrim:Arcadia's Cauldron") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Alchemy (Expert)](/wiki/Skyrim:Alchemy "Alchemy (Expert)") |
| [Babette](/wiki/Skyrim:Babette "Skyrim:Babette") | [Dark Brotherhood Sanctuary](/wiki/Skyrim:Dark_Brotherhood_Sanctuary "Skyrim:Dark Brotherhood Sanctuary") or [Dawnstar Sanctuary](/wiki/Skyrim:Dawnstar_Sanctuary "Skyrim:Dawnstar Sanctuary") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Alchemy (Master)](/wiki/Skyrim:Alchemy "Alchemy (Master)") |
| [Balimund](/wiki/Skyrim:Balimund "Skyrim:Balimund") | [The Scorched Hammer](/wiki/Skyrim:The_Scorched_Hammer "Skyrim:The Scorched Hammer") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Smithing (Expert)](/wiki/Skyrim:Smithing "Smithing (Expert)") |
| [Colette Marence](/wiki/Skyrim:Colette_Marence "Skyrim:Colette Marence") | [College of Winterhold](/wiki/Skyrim:College_of_Winterhold_(place) "Skyrim:College of Winterhold (place)") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Restoration (Expert)](/wiki/Skyrim:Restoration "Restoration (Expert)") |
| [Drevis Neloren](/wiki/Skyrim:Drevis_Neloren "Skyrim:Drevis Neloren") | [College of Winterhold](/wiki/Skyrim:College_of_Winterhold_(place) "Skyrim:College of Winterhold (place)") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Illusion (Master)](/wiki/Skyrim:Illusion "Illusion (Master)") |
| [Eorlund Gray-Mane](/wiki/Skyrim:Eorlund_Gray-Mane "Skyrim:Eorlund Gray-Mane") | [Skyforge](/wiki/Skyrim:Skyforge "Skyrim:Skyforge") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Smithing (Master)](/wiki/Skyrim:Smithing "Smithing (Master)") |
| [Falion](/wiki/Skyrim:Falion "Skyrim:Falion") | [Falion's House](/wiki/Skyrim:Falion%27s_House "Skyrim:Falion's House") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Conjuration (Master)](/wiki/Skyrim:Conjuration "Conjuration (Master)") |
| [Faralda](/wiki/Skyrim:Faralda "Skyrim:Faralda") | [College of Winterhold](/wiki/Skyrim:College_of_Winterhold_(place) "Skyrim:College of Winterhold (place)") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Destruction (Master)](/wiki/Skyrim:Destruction "Destruction (Master)") |
| [Florentius Baenius](/wiki/Skyrim:Florentius_Baenius "Skyrim:Florentius Baenius")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Restoration (Master)](/wiki/Skyrim:Restoration "Restoration (Master)") |
| [Gharol](/wiki/Skyrim:Gharol "Skyrim:Gharol") | [Dushnikh Yal](/wiki/Skyrim:Dushnikh_Yal "Skyrim:Dushnikh Yal") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Heavy Armor (Expert)](/wiki/Skyrim:Heavy_Armor "Heavy Armor (Expert)") |
| [Ghorza gra-Bagol](/wiki/Skyrim:Ghorza_gra-Bagol "Skyrim:Ghorza gra-Bagol") | [Markarth](/wiki/Skyrim:Markarth "Skyrim:Markarth") | [Trainer (Common)](/wiki/Skyrim:Trainers "Trainer (Common)")[Smithing (Common)](/wiki/Skyrim:Smithing "Smithing (Common)") |
| [Grelka](/wiki/Skyrim:Grelka "Skyrim:Grelka") | [Riften](/wiki/Skyrim:Riften "Skyrim:Riften") marketplace | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Light Armor (Expert)](/wiki/Skyrim:Light_Armor "Light Armor (Expert)") |
| [Gunmar](/wiki/Skyrim:Gunmar "Skyrim:Gunmar")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Smithing (Master)](/wiki/Skyrim:Smithing "Smithing (Master)") |
| [Lami](/wiki/Skyrim:Lami "Skyrim:Lami") | [Thaumaturgist's Hut](/wiki/Skyrim:Thaumaturgist%27s_Hut "Skyrim:Thaumaturgist's Hut") | [Trainer (Common)](/wiki/Skyrim:Trainers "Trainer (Common)")[Alchemy (Common)](/wiki/Skyrim:Alchemy "Alchemy (Common)") |
| [Ma'jhad](/wiki/Skyrim:Ma%27jhad "Skyrim:Ma'jhad") | [Ma'dran](/wiki/Skyrim:Ma%27dran "Skyrim:Ma'dran")'s [Khajiit caravan](/wiki/Skyrim:Khajiit_Traders "Skyrim:Khajiit Traders") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Lockpicking (Expert)](/wiki/Skyrim:Lockpicking "Lockpicking (Expert)") |
| [Milore Ienth](/wiki/Skyrim:Milore_Ienth "Skyrim:Milore Ienth")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Raven Rock](/wiki/Skyrim:Raven_Rock "Skyrim:Raven Rock")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Alchemy (Expert)](/wiki/Skyrim:Alchemy "Alchemy (Expert)") |
| [Neloth](/wiki/Skyrim:Neloth "Skyrim:Neloth")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Tel Mithryn](/wiki/Skyrim:Tel_Mithryn_(tower) "Skyrim:Tel Mithryn (tower)")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Enchanting (Master)](/wiki/Skyrim:Enchanting "Enchanting (Master)") |
| [Phinis Gestor](/wiki/Skyrim:Phinis_Gestor "Skyrim:Phinis Gestor") | [College of Winterhold](/wiki/Skyrim:College_of_Winterhold_(place) "Skyrim:College of Winterhold (place)") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Conjuration (Expert)](/wiki/Skyrim:Conjuration "Conjuration (Expert)") |
| [Revyn Sadri](/wiki/Skyrim:Revyn_Sadri "Skyrim:Revyn Sadri") | [Sadri's Used Wares](/wiki/Skyrim:Sadri%27s_Used_Wares "Skyrim:Sadri's Used Wares") | [Trainer (Common)](/wiki/Skyrim:Trainers "Trainer (Common)")[Speech (Common)](/wiki/Skyrim:Speech "Speech (Common)") |
| [Ronthil](/wiki/Skyrim:Ronthil "Skyrim:Ronthil")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Volkihar Keep](/wiki/Skyrim:Volkihar_Keep "Skyrim:Volkihar Keep")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Speech (Expert)](/wiki/Skyrim:Speech "Speech (Expert)") |
| [Sorine Jurard](/wiki/Skyrim:Sorine_Jurard "Skyrim:Sorine Jurard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Fort Dawnguard](/wiki/Skyrim:Fort_Dawnguard "Skyrim:Fort Dawnguard")[DG](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Archery (Master)](/wiki/Skyrim:Archery "Archery (Master)") |
| [Sybille Stentor](/wiki/Skyrim:Sybille_Stentor "Skyrim:Sybille Stentor") | [Blue Palace](/wiki/Skyrim:Blue_Palace "Skyrim:Blue Palace") | [Trainer (Expert)](/wiki/Skyrim:Trainers "Trainer (Expert)")[Destruction (Expert)](/wiki/Skyrim:Destruction "Destruction (Expert)") |
| [Talvas Fathryon](/wiki/Skyrim:Talvas_Fathryon "Skyrim:Talvas Fathryon")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Tel Mithryn](/wiki/Skyrim:Tel_Mithryn_(tower) "Skyrim:Tel Mithryn (tower)")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Conjuration (Master)](/wiki/Skyrim:Conjuration "Conjuration (Master)") |
| [Tolfdir](/wiki/Skyrim:Tolfdir "Skyrim:Tolfdir") | [College of Winterhold](/wiki/Skyrim:College_of_Winterhold_(place) "Skyrim:College of Winterhold (place)") | [Trainer (Master)](/wiki/Skyrim:Trainers "Trainer (Master)")[Alteration (Master)](/wiki/Skyrim:Alteration "Alteration (Master)") |
| [Wuunferth the Unliving](/wiki/Skyrim:Wuunferth_the_Unliving "Skyrim:Wuunferth the Unliving") | [Palace of the Kings](/wiki/Skyrim:Palace_of_the_Kings "Skyrim:Palace of the Kings") | [Trainer (Common)](/wiki/Skyrim:Trainers "Trainer (Common)")[Destruction (Common)](/wiki/Skyrim:Destruction "Destruction (Common)") |

## Notes

- If you steal enough of a merchant's possessions, they may send [Hired Thugs](/wiki/Skyrim:Hired_Thug "Skyrim:Hired Thug") after you. Some may also view knocking display items down and [shouting](/wiki/Skyrim:Shouts "Skyrim:Shouts") in their shop as reason enough.
- If a merchant lives in his or her shop and you go beyond the counter to their room, they will follow you around.
- [Torches](/wiki/Skyrim:Torch "Skyrim:Torch") cannot be bought from merchants or sold to them, no matter how high your [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") skill is or how many perks related to merchants are active.
- Your spouse can start handing out profits before ever moving to your house and informing you they're opening a store.
- Unlike in *[Morrowind](/wiki/Morrowind:Merchants "Morrowind:Merchants")*, merchants in *Skyrim* don't care if you have any [moon sugar](/wiki/Skyrim:Moon_Sugar "Skyrim:Moon Sugar") or [skooma](/wiki/Skyrim:Skooma "Skyrim:Skooma") in your inventory. There is a small number of merchants who sell them as well.
- Merchants who are also [Trainers](/wiki/Skyrim:Trainers "Skyrim:Trainers") add the gold that you pay them for training to the gold they carry in their personal inventory. As such, it then becomes available to be used for bartering as all personal items not equipped can be purchased from a merchant. However, most merchants have a cap on their personal gold which is put into effect when you enter their stores, so if you leave the store and come back later, the gold will have disappeared. Notable exceptions to this are the merchant trainers added by the [Dawnguard](/wiki/Skyrim:Dawnguard "Skyrim:Dawnguard") add-on.
- [Curate Melita](/wiki/Skyrim:Curate_Melita "Skyrim:Curate Melita")[CC](/wiki/Skyrim:Ghosts_of_the_Tribunal "Skyrim:Ghosts of the Tribunal") is supposed to be a [Restoration](/wiki/Skyrim:Restoration "Skyrim:Restoration") trainer and does have a conversation about that, but you can never receive training from her, even with a low Restoration skill.
- Resetting the [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") perk tree using the Black Book [Waking Dreams](/wiki/Skyrim:Black_Book:_Waking_Dreams_(book) "Skyrim:Black Book: Waking Dreams (book)")[DB](/wiki/Skyrim:Dragonborn "Skyrim:Dragonborn") does not affect investments that you may have previously made with merchants.
- If you side with the [Dawnguard](/wiki/Skyrim:Dawnguard_(faction) "Skyrim:Dawnguard (faction)") and become a vampire later, the Fort Dawnguard merchants won't sell anything until you [cure yourself](/wiki/Skyrim:Rising_at_Dawn "Skyrim:Rising at Dawn"). Likewise, if you side with the [Volkihar family](/wiki/Skyrim:Volkihar_Vampire_Clan "Skyrim:Volkihar Vampire Clan") and [cure yourself](/wiki/Skyrim:Rising_at_Dawn "Skyrim:Rising at Dawn") later, the Volkihar Keep merchants won't sell anything until your vampirism is restored.
- If you move your spouse to one of the [homesteads](/wiki/Skyrim:Houses#Hearthfire_HousesHF "Skyrim:Houses") added by the [Hearthfire](/wiki/Skyrim:Hearthfire "Skyrim:Hearthfire") add-on, they will often wander around outside the house where their merchant chest will not be available. To engage in trade with your spouse, wait until they go inside, or if they are a follower you can ask them to follow you and lead them inside.
- Because merchant inventory is not written to the save file, a merchant is more-or-less guaranteed to have a different inventory and a different amount of gold each time you load a save. The exception is that if you quick-save, and then quick-load while the in-memory merchant data is still valid, the merchant inventory will be the same as before the quick-load. However, if you take an action that invalidates the merchant's in-memory data, such as attacking the merchant, the subsequent quick-load will have a regenerated inventory, the same as if you had shut down and then restarted the game.

## Bugs

- If a merchant is talking to you as you are leaving their store, they will exit along with you, re-enter their store, lock the doors and close for the day.
- If you attack a merchant and reload immediately before the attack occurs, or if you save, then attack a merchant and reload, their inventory should reset. **?**
  - This method won't work with your spouse.
  - Don't attack a merchant and use a [Calm](/wiki/Skyrim:Calm "Skyrim:Calm") spell on them, or their inventory won't reset.
- Selecting the *Fence* perk may allow you to sell stolen goods to any merchant, not just those you have invested in as the perk description states. **?**
- When resetting your [Speech](/wiki/Skyrim:Speech "Skyrim:Speech") skill, you still retain your ability to invest in merchants, without having to have that perk or having a speech skill high enough to be able to get this perk. This is also true for *Master Trader*—all related merchants will still have 1000 more gold even after you lose the perk. **?**
- The Investor perk may prevent merchants you invest with from receiving the extra gold properly.
  - The [Official Skyrim Patch](/wiki/Skyrim:Patch "Skyrim:Patch"), version 1.9, fixes this bug.
- You can buy from hunters, your money will be reduced normally and you will get the item, but when selling to them your item will disappear and you will get no money.
  - The [Official Skyrim Special Edition Patch](/wiki/Skyrim:Special_Edition_Patch "Skyrim:Special Edition Patch"), version 1.6.1130.0, fixes this bug.
- Some of the merchants may "forget" that you invested in their shop and lose the option for having extra buying gold. This appears to affect female alchemy merchants much more than male merchants or merchants of general goods stores (e.g. Angeline's Aromatics in Solitude will never remember an investment).
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.1, fixes this bug.
- Each rank of the Haggling perk delivers inconsistent results on prices. Specifically, Rank 1 only gives you a 9% discount when it should be 10%. Rank 2 only gives you a 13% discount when it should be 15%. Rank 3 only gives you a 17% discount when it should be 20%. Rank 4 only gives you a 20% discount when it should be 25%. Rank 5 only gives you a 23% discount when it should be 30%.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.2.6, addresses this issue. The purchase prices were using incorrect decimal values to produce the expected discounts.
  - All of the selling bonuses on these perks are correct regardless whether you have the patch or not.
- Allure only provides a 9% bonus when buying items instead of a 10% bonus as is stated in the description.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch"), version 3.0.11, fixes this bug.
- The Lover's Insight reward from Black Book: The Winds of Change only gives a 9% bonus to prices instead of the advertised 10%.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Dragonborn Patch](/wiki/Skyrim_Mod:Unofficial_Dragonborn_Patch "Skyrim Mod:Unofficial Dragonborn Patch"), version 1.0.5, fixes this bug.
- Several merchants may miss the bonus gold from the Master Trader perk despite the perk specifically stating ALL merchants in the world should have it.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.3.2, fixes this bug.
- Innkeepers can fail to headtrack you upon entering the building due to the WITavernGreeting scenes not having headtracking set at all.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 1.3.3, fixes this bug.
- Ysolda and Camilla may both accept investments in their shops after being married, which makes little sense considering they're no longer going to be running the shops they are assigned as backups to.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.1, fixes this bug.
- Dwemer Scrap Metal is not classified as ores or ingots by merchants, and therefore cannot be sold to blacksmiths or jewelers without the [Merchant perk](/wiki/Skyrim:Merchant_(perk) "Skyrim:Merchant (perk)").
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.5, fixes this bug.
  - This bug is also fixed with version 1.6.1130 of the [Official Skyrim Special Edition Patch.](/wiki/Skyrim:Special_Edition_Patch "Skyrim:Special Edition Patch")
- Hunter merchants may attack your [horse](/wiki/Skyrim:Horses "Skyrim:Horses") even though your horse is your ally.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.7, addresses this issue. This was due to incomplete faction relationships.
- Spouse dialogue saying they're starting a new store repeats itself even though the "say once" flag is checked.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Patch "Skyrim Mod:Unofficial Skyrim Patch"), version 2.0.8, addresses this issue. A script variable has been added to block this after the first use as a workaround to the "say once flag".
- Despite being able to run a shop from one of the Hearthfire properties, your spouse never actually says they're going to do that if this is the first house you move them to because the dialogue conditions did not include the HF locations.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Hearthfire Patch](/wiki/Skyrim_Mod:Unofficial_Hearthfire_Patch "Skyrim Mod:Unofficial Hearthfire Patch"), version 2.0.1, fixes this bug.

\* Trading with vendors becomes unreliable when their gold reserves exceeds 32,767. The game's internal trading mechanism mistakenly treats their gold quantity as a [signed 16-bit integer](https://en.wikipedia.org/wiki/Integer_(computer_science)#Short_integer "wikipedia:Integer (computer science)"), whose value could be between -32768 and 32767. If you buy a lot of expensive items or receive high-level skill training, so much so that their gold reserve goes beyond 32,767, an [Integer overflow](https://en.wikipedia.org/wiki/Integer_overflow "wikipedia:Integer overflow") bug occurs. Thus, you can still sell them items, but you lose the item without gaining any gold. Complicating the matter is the fact that each vendor's gold reserve is the sum of gold in their inventory plus the gold in their chests.

:   - A community-developed bug fix is available as a mod called "[Barter Limit Fix](https://www.nexusmods.com/skyrimspecialedition/mods/77173)."

- Merchants can sometimes lose the dialogue option "What have you got for sale?" making it impossible to trade with them.
  - [![On PC](//images.uesp.net/d/d7/Computer.svg)](https://en.wikipedia.org/wiki/PC_game "PC") You can try the following to resolve the issue:
    - open the console
    - enter the console command `startquest dialoguegeneric`
    - press enter
    - close the console
    - wait 1 to 2 minutes then make a new save file and then load from that save file
    - check the merchant and see if the dialogue option is back
- The AI counter markers in various shops either lack ownership or have incorrect ownership assigned, causing NPCs other than the vendors to use them.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch"), version 3.0.1, fixes this bug.
- The spouse merchant chests are missing an investor perk formlist, so that they never gain a permanent 500 gold increase after investing. This also means that if you marry an NPC who was already a merchant, the 500 gold bonus is being applied to a merchant chest they no longer have access to, rather than the spouse merchant chest they're currently using.
  - ![PC Only](//images.uesp.net/d/d7/Computer.svg "PC Only") The [Unofficial Skyrim Legendary Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Legendary_Edition_Patch "Skyrim Mod:Unofficial Skyrim Legendary Edition Patch"), version 3.0.1, addresses this issue. The invest prompt with Taarie, Balimund, Muiri, Ghorza, Revyn Sadri, Filnjar, Quintus Navale, Dravynea, and Moth gro-Bagol will be removed once you marry one of them. The way the vendor stack works makes it impractical to continue to allow the option since it won't get directed to the proper place anyway.
- Investor perk dialogue does not use the correct condition checks to determine the amount of gold you need to be able to invest.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.4, fixes this bug.
- The loot list for expert level spell tomes in dungeons incorrectly uses a global variable setting that's intended to be used on vendor inventories.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.2.5, fixes this bug.
- Your spouse will be unable to talk to you about opening a store if the house you chose to move into after getting married was one of the Creation Club houses. Options did not exist for this to happen.
  - The [Unofficial Skyrim Special Edition Patch](/wiki/Skyrim_Mod:Unofficial_Skyrim_Special_Edition_Patch "Skyrim Mod:Unofficial Skyrim Special Edition Patch"), version 4.3.5, fixes this bug.
