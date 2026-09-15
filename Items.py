import random

# Creating an item class and characteristics
class Items:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# Creating an item objects
Bone = Items("Bone", "a Monster bone. Might come in handy", 10)

Stick = Items("Stick", "A smooth handle for future axe, pickaxe, or something similar. Doesn't sound very useful, but with enough imagination, it might prove handy.", 20)

Rope = Items("Rope", " A three-meter length of rope. It looks almost unused, as if someone placed it here recently. With the right skill, it could be very useful", 15)

Dagger = Items("Dagger", "A small silver dagger. It looks worn, but still usable. Compared to your iron sword, it may not seem like a great option, but it could give you an advantage against enemies.", 15)

Horseshoe = Items("Horseshoe", "Looks very well crafted. likely made by a renowned blacksmith. It may not seem useful, but if you are superstitious, it might bring you a bit of luck.", 10)

#Function for spawning random item.
def randomItem():

    item = [Bone, Stick, Rope, Dagger, Horseshoe]
    
    return random.choice(item)
