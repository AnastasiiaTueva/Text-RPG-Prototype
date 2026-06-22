import random

# Creating a character class and characteristics

class Character:

    def __init__(self, health, minDamage, maxDamage, XP):

        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.XP = XP

        self.luck = 1
        self.strength = 1
        self.agility = 1
        self.intelligence = 1

    # Function for creating random damage to a character
    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)

# Creating a main character object
Hero = Character(20, 1, 4, 0)
