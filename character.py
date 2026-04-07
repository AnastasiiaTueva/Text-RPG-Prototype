import random

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

    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)

Hero = Character(20, 1, 4, 0)
