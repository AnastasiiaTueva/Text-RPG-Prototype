import random 

class Mob:

    def __init__(self, health, damage, XP):
        self.health = health
        self.damage = damage
        self.XP = XP

Skeleton = Mob(20, random.randint(1,2), 50)
