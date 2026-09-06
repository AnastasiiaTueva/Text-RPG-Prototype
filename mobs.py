import random 


# Creating a monster class and characteristics
class Mob:

    def __init__(self, name, health, minDamage,maxDamage, XP):
        self.name = name
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.XP = XP

    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)


# Creating randomization of monster spawns
def randomMob():
    Mobs = [
            Mob("Skeleton", 20, 1, 2, 50),
            Mob("Slime", 15, 1, 2, 25),
            Mob("Zombie", 15, 1, 2, 25)
    ]
    return random.choice(Mobs)
