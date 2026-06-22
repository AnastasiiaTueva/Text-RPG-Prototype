import random 


# Creating a monster class and characteristics
class Mob:

    def __init__(self, health, minDamage,maxDamage, XP):
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.XP = XP

    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)


# Creating a Skeleton object
Skeleton = Mob(20, 1, 4, 50)


# Creating a Slime object
Slime = Mob(15, 1, 2, 25)

# Creating randomization of monster spawns
def randomMob():
    Mobs = [Skeleton, Slime]
    random_mobs = random.choice(Mobs)
    print(f"\nYou encountered {random_mobs}")
