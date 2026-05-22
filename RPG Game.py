import random

choice = ""

def give_options():
    if choice == "inventory" or choice == "i" or choice == "inv":
        inventory.sort()
        print(inventory)
    if choice == "inspect inv" or choice == "ii" or choice == "inspect inventory":
        inventory_inspect_choice = input("What item would you like to inspect? ")
    if choice == "spells" or choice == "spelllist" or choice == "spell list":
        spell_list.sort
        print(spell_list)
    if choice == "skills" or choice == "skilllist" or choice == "skill list":
        skill_list.sort
        print(skill_list)
    if choice == "options":
        print("inventory, inspect inventory, spells, skills")

#Player Stats

max_health = 100
health = 100
max_mana = 10
mana = 10
inventory = []
spell_list = []
skill_list = []
level = 1
blood_alcohol_content = 0.00
coins = 100
current_class = ""
current_race = ""
game_stage = "Start Screen"
character_name = ""
acceptable_classes = ["warrior", "mage", "archer", "alchemist", "ritualist", "artificer"]
acceptable_races = ["human", "elf", "orc", "goblin", "skyfoul", "clockwork golem"]
choice = ""
alt_choice = ""

#Area Stats

current_location = "The Argon Axolotl"
current_room = "Main Dinning Hall"
year = 1436
month = 3
day = 22
hour = 11
minute = 36

#Magic Stats

fire_affinity = 0
water_affinity = 0
electric_affinity = 0
poison_affinity = 0
earth_affinity = 0
arcane_affinity = 0
silk_affinity = 0

class spells:
    def __init__(self, spell, level, acquired):
        self.spell = spell
        self.level = level
        self.acquired = acquired
        
# Skills

class skills:
    def __init__(self, skill, level, acquired, activated, experience):
        self.skill = skill
        self.level = level
        self.acquired = acquired
        self.activated = activated
        self.experience = experience

farming_skill = skills("Farming", 0, False, False, 0)
mining_skill = skills("Mining", 0, False, False, 0)
taunting_scream = skills("Taunting Scream", 0, False, True, 0)
sword_skill = skills("Sword Combat Training", 0, False, False, 0)
bow_skill = skills("Bow Combat Training", 0, False, False, 0)
crossbow_skill = skills("Crossbow Combat Training", 0, False, False, 0)
hand_combat_skill = skills("Hand-to-hand Combat Training", 0, False, False, 0)
alchemy_skill = skills("Alchemy", 0, False, False, 0)
chemistry_skill = skills("Chemistry", 0, False, False, 0)
ritual_skill = skills("Ritualism", 0, False, False, 0)
smithing_skill = skills("Smithing", 0, False, False, 0)
poison_resistance_skill = skills("Poison Resistance", 0, False, False, 0)
alchohol_tolerance_skill = skills("Achohol Tolerance", 0, False, False, 0)

# Actual Gameplay

while game_stage == "Start Screen":
    start_choice = input('Type "Start" to start the game! ')
    if start_choice == "Start" or start_choice == "start":
        game_stage = "Character Creation"
    elif start_choice == "SHAW!" or start_choice == "ADINO!" or start_choice == "HEGALE!" or start_choice == "GARAMA!" or start_choice == "GITGUD!":
        character_name = "Hornet"
        current_race = "spider-wyrm"
        current_class = "weaver"
        silk_affinity = 10
        game_stage = "Gameplay Loop"
    elif start_choice == "UUDDLRLRABSELECTSTART" or start_choice == "UpUpDownDownLeftRightLeftRightABSelectStart":
        max_health = 10000
        health = 10000
        max_mana = 10000
        mana = 10000

while game_stage == "Character Creation":
    while character_name == "":
        character_name = input("Please input a name for your character: ")
    while current_race not in acceptable_races:
        current_race = input("Please select a race or type list for acceptable races ").lower()
        if current_race == "list":
            print(acceptable_races)
    while current_class not in acceptable_classes:
        current_class = input("Please select a class or type list for acceptable classes ").lower()
        if current_class == "list":
            print(acceptable_classes)
    if current_race in acceptable_races and current_class in acceptable_classes:
        game_stage = "Gameplay Loop"

while game_stage == "Gameplay Loop":

    while current_location == "The Argon Axolotl":
        while current_room == "Main Dinning Hall":
            print("You are in the main dinning hall of the Argon Axolotl tavern")
            choice = input("What will you do? ").lower()
            give_options()
            if choice == "talk" or choice == "t":
                print("Hey there, I'm Bob the Bartender")
                print("I sell drinks and stuff")
                alt_choice == input("Would you like to buy a drink? Only four coins. ").lower()
                if alt_choice == "yes" or alt_choice == "y" and coins >= 4:
                    print("Great, that'll be four coins")
                    coins -= 4
                    inventory.append("Flagon of beer")
                elif alt_choice == "yes" or alt_choice == "y" and coins < 4:
                    print("Nope you're too broke")
                else:
                    print("That's fine, it's not like I worked hard on it or anything")
            if choice == "leave":
                current_location = "Town of Greyshard"
                current_room = "Town Square"

    while current_location == "Town of Greyshard":
        while current_room == "Town Square":
            print("You are in the town square of the Town of Greyshard")
            print("You can go to the following areas: Tavern, Blacksmith, General Store")
            give_options()
            if choice == "Tavern":
                current_location = "The Argon Axolotl"
                current_room = "Main Dinning Hall"
            if choice == "Blacksmith":
                current_location = "The Greyshard Smithy"
                current_room = "Shop Front"
            if choice == "General Store":
                current_location = "The Greyshard General Store"
                current_room = "Shop Front"

    while current_location == "The Greyshard Smithy":
        while current_room == "Shop Front":
            print("Hello, I am a blacksmith with many wares")
            print("Here is what I have with their prices:")
            print("Steel Axe (12)")
            print("Iron Axe (11)")
            print("Iron Sword (10)")
            print("Steel Spear (12)")
            print("Iron Spear (11)")
            give_options()




