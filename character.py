import random


class Character:

    def __init__(self, health, damage, XP):

        self.health = health
        self.damage = damage
        self.XP = XP

Hero = Character(20, random.randint(1,3), 0)
