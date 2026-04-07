import random 

class Mob:

    def __init__(self, health, minDamage,maxDamage, XP):
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.XP = XP

    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)

Skeleton = Mob(20, 1, 2, 50)
