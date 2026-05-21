import flask
import random

def give_options():
    choice = input("What will you do? ").lower()
    if choice == "inventory" or choice == "i" or choice == "inv":
        inventory.sort()
        print(inventory)
    if choice == "inspect_inv" or choice == "ii" or choice == "inspect_inventory":
        inv_choice = input("What item would you like to inspect? ")
    if choice == "spells" or choice == "spelllist" or choice == "spell list":
        spell_list.sort
        print(spell_list)
    if choice == "skills" or choice == "skilllist" or choice == "skill list":
        skill_list.sort
        print(skill_list)

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
current_class = ""
current_race = ""
game_stage = "Start Screen"
character_name = ""
acceptable_classes = ["warrior", "mage", "archer", "alchemist", "ritualist", "artificer"]
acceptable_races = ["human", "elf", "orc", "goblin", "skyfoul", "clockwork golem"]

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
    while current_race in acceptable_races and current_class in acceptable_classes:
        game_stage = "Gameplay Loop"

while game_stage == "Gameplay Loop":

    while current_room == "Main Dinning Hall" and current_location == "The Argon Axolotl":
        print("You wake up in a tavern")
        give_options()
