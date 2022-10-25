

from random import randint
from random import random
from secrets import choice
import secrets

# Creating the warrior class with starting stats
class Warrior:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_to_level = 750 + (self.level * 250)
        self.maxhp = 40 + (4 * self.level)
        self.hp = 40 + (4 * self.level)
        self.maxmana = 10 + (1 * self.level)
        self.mana = 10 + (1 * self.level)
        self.defense = 0 + (3 * self.level)
        self.attack_damage = 0 + randint((3+self.level), (7+self.level))
        self.weapons = []
        self.armor = []
        self.health_potions = 1
        self.mana_potions = 1

    # Will be able to use repr to give current status of the player including level, hp, mana, and exp to next level.
    def __repr__(self):
        return "{name} is a level {level} Warrior. {name} currently has {hp}hp left and {mana} mana left. {name} requires {exp}exp to the next level".format(name=self.name, level=str(self.level), hp=str(self.hp), mana=str(self.mana), exp=str((self.exp_to_level-self.exp)))

    # Creating method for character to level up.
    def level_up(self):
        if self.exp >= self.exp_to_level:
            self.level += 1
            self.exp = (self.exp - self.exp_to_level)
            print("Congradulations! {name} has leveled up to level {level}".format(name = self.name, level = self.level))
    
    # Creating method for character to heal to max health and mana when going to rest.
    def rest(self):
        self.hp = self.maxhp
        self.mana = self.maxmana
        print("{name} has rested for the night and feels refreshed.".format(name = self.name))

    # Creating method for character to deal damage to the target based on characters attack damage and targets defense
    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            self.exp += target.expgive
            self.level_up()
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died. You gain {exp}exp".format(name = self.name, damage = attack_damage, target_name = target.name, exp = str(target.expgive)))
        elif attack_damage < target.hp:
            target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))

    # Creating method for character to restore mana using mana potion
    def use_mana_pot(self):
        if self.mana_potions == 0:
            print("Sorry you are out of mana potions!")
        elif self.mana_potions > 0:
            self.mana = self.maxmana
            self.mana_potions -= 1
            print("{name} uses a mana potion and has their mana fully restored!".format(name = self.name))
            

    # Creating method for character to restore health using health potion
    def use_hp_pot(self):
        if self.health_potions == 0:
            print("Sorry you are out of health potions!")
        elif self.health_potions > 0:
            self.hp = self._hpmax
            self.health_potions -= 1
            print("{name} uses a mana potion and has his mana fully restored!".format(name = self.name))
    




# Creating a base zombie and its stats
class Zombie:
    def __init__(self, level = randint(1,3)):
        self.level = level
        self.name = "Zombie"
        self.hp = 20 + (2 * self.level)
        self.attack_damage = randint(1 + (self.level), (5 + self.level))
        self.defense = 0
        self.weapons = []
        self.armor = []
        self.expgive = 100 + (self.level * 25)
        
    # Creating method for Zombie to deal damage to the target based on attack damage and targets defense
    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died. You lose".format(name = self.name, damage = attack_damage, target_name = target.name))
            game_over = True
        elif attack_damage < target.hp:
            if attack_damage < 0:
                target.hp -= 0
                print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))
            else:
                target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))



class Skeleton:
    def __init__(self, level = randint(3,5)):
        self.level = level
        self.name = "Skeleton"
        self.hp = 30 + (2 * self.level)
        self.attack_damage = randint((2 + self.level), (5 + self.level))
        self.defense = 1
        self.weapons = []
        self.armor = []
        self.expgive = 125 + (self.level * 25)

    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died. You lose".format(name = self.name, damage = attack_damage, target_name = target.name))
            game_over = True
        elif attack_damage < target.hp:
            if attack_damage < 0:
                target.hp -= 0
                print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))
            else:
                target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))



class Vampire:
    def __init__(self, level = randint(5,8)):
        self.level = level
        self.name = "Vampire"
        self.hp = 35 + (2 * self.level)
        self.attack_damage = randint((2 + self.level), (4 + self.level))
        self.defense = 1
        self.weapons = []
        self.armor = []
        self.expgive = 150 + (self.level * 25)

    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died. You lose".format(name = self.name, damage = attack_damage, target_name = target.name))
            game_over = True
        elif attack_damage < target.hp:
            if attack_damage < 0:
                target.hp -= 0
                print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))
            else:
                target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))


class Dracula:
    def __init__(self, level = 10):
        self.level = level
        self.name = "Dracula"
        self.hp = 30 + (2 * self.level)
        self.attack_damage = randint((2 + self.level), (4 + self.level))
        self.defense = 1
        self.weapons = []
        self.armor = []
        self.expgive = 150 + (self.level * 25)

    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died. You lose".format(name = self.name, damage = attack_damage, target_name = target.name))
            game_over = True
        elif attack_damage < target.hp:
            if attack_damage < 0:
                target.hp -= 0
                print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))
            else:
                target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))






# Starts the game with getting name for character
player_name = input("In a world over run by monsters there is a town which has been holding struggling to survive. It is up to you adventurer to save the town. What is your name?")

# Creates the player as a Warrior using name
player1 = Warrior(player_name)

print("You may enter the dungeon whenever you are ready by typing \"dungeon\"")
print("If you are low on health or mana you can always go back to town by typing \"town\" to rest and recover")
print("If you would like to check your status including level, hp, mana, and experience needed to the next level type \"status\"")
print("If you find yourself brace enough to take on Dracula who is haunting this town type \"Castle\" to confront him!")

# creating variable to keep while loop running to repeat available inputs, until a game over condition is met.
game_over = False
battle_over = False

# Keeps game running unless a game_over contition is met
while game_over == False:
    # Created a variable for raw input to run allowed methods/game
    raw_input = input(" ")
    
    
    
    # Start of battle options by typing dungeon into the console
    if raw_input == "dungeon":
        # set condition to false to allow for loop to run until player or monster is at 0 hp
        battle_over = False
        # Creating seperate loop for player at lower level to fight lower level monsters
        
        if player1.level <= 3:
            # Create a new zombie with random level to fight player
            monster = Zombie()
            while battle_over == False:
                # Checks to see if monster hp is at 0 to prevent another loop
                if monster.hp == 0:
                    battle_over = True
                else:
                    player1.attack(monster)
                    # prevents monster from attacking player if monster is at 0 hp after taking hit
                    if monster.hp > 0:
                        monster.attack(player1)
        
        elif player1.level < 6:
            # Create a new skeleton with random level to fight player
            monster = Skeleton()
            while battle_over == False:
                # Checks to see if monster hp is at 0 to prevent another loop
                if monster.hp == 0:
                    battle_over = True
                else:
                    player1.attack(monster)
                    # prevents monster from attacking player if monster is at 0 hp after taking hit
                    if monster.hp > 0:
                        monster.attack(player1)

        elif player1.level > 8:
            # Create a new skeleton with random level to fight player
            monster = Vampire()
            while battle_over == False:
                # Checks to see if monster hp is at 0 to prevent another loop
                if monster.hp == 0:
                    battle_over = True
                else:
                    player1.attack(monster)
                    # prevents monster from attacking player if monster is at 0 hp after taking hit
                    if monster.hp > 0:
                        monster.attack(player1)


    elif raw_input == "castle":
        # set condition to false to allow for loop to run until player or monster is at 0 hp
        battle_over = False
        # Creating seperate loop for player at lower level to fight lower level monsters
        
        # Create a new zombie with random level to fight player
        monster = Dracula()
        while battle_over == False:
            # Checks to see if monster hp is at 0 to prevent another loop
            if monster.hp == 0:
                battle_over = True
            else:
                player1.attack(monster)
                # prevents monster from attacking player if monster is at 0 hp after taking hit
                if monster.hp > 0:
                    monster.attack(player1)



    elif raw_input == "town":
        player1.rest()
    elif raw_input == "status":
        print(repr(player1))
    elif raw_input == "quit":
        game_over = True