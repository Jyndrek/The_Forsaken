# Creating the warrior class with starting stats

from random import randint


class Warrior:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_to_level = 750 + (self.level * 250)
        self.maxhp = 0 + (2 * self.level)
        self.hp = 0 + (2 * self.level)
        self.maxmana = 0 + (1 * self.level)
        self.mana = 0 + (1 * self.level)
        self.defense = 0 + (2 * self.level)
        self.attack_damage = 0 + randint((3+self.level), (7+self.level))
        self.weapons = []
        self.armor = []
        self.health_potions = 1
        self.mana_potions = 1

    # Creating method for character to level up.
    def level_up(self):
        if self.exp >= self.exp_to_level:
            self.level += 1
            self.atrpt += 5
            print("Congradulations! {name} has leveled up to level {leevl}".format(name = self.name, level = self.level))
    
    # Creating method for character to heal to max health and mana when going to rest.
    def rest(self):
        self.hp = self.maxhp
        self.mana = self.maxmana

    # Creating method for character to deal damage to the target based on characters attack damage and targets defense
    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        if attack_damage >= target.hp:
            target.hp = 0
            print("{name} dealt {damage} damage to {target_name}. {target_name} has died".format(name = self.name, damage = attack_damage, target_name = target.name))
        elif attack_damage < target.hp:
            target.hp -= attack_damage
            print("{name} dealt {damage} damage to {target_name}. {target_name} has {target_hp} hp left!".format(name = self.name, damage = attack_damage, target_name = target.name, target_hp = target.hp))

    # Creating method for character to restore mana using mana potion
    def use_mana_pot(self):
        self.mana = self.maxmana

    # Creating method for character to restore health using health potion
    def use_hp_pot(self):
        self.hp = self.maxhp
    




# Creating a base zombie and its stats
class Zombie:
    def __init__(self, level = 1):
        self.level = level
        self.name = "Zombie"
        self.hp = 30
        self.attack_damage = range((self.level), (3 + self.level))
        self.defense = 0
        self.weapons = []
        self.armor = []
        self.expgive = 100 + (self.level * 25)
        
    # Creating method for Zombie to deal damage to the target based on attack damage and targets defense
    def attack(self, target):
        attack_damage = self.attack_damage - target.defense
        target.hp -= attack_damage













# Game Testing
player1_name = input("Please enter the name of your warrior")
player1 = Warrior(player1_name)
monster = Zombie()

player1.attack(monster)

