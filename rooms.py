import Locations
import random
import text
import character
import mobs
import food
import Items
import hotkeys

def newRoom():
    global Rsize, Rtype
    Rsize, Rtype = Locations.locationGen()

def Dsize():
    if Rsize == "middle":
        if random.random() < 0.2 * character.Hero.agility:
            text.typetext(f"The {mobs.mob.name} attacked you, but you dodged.")
        else:
            character.Hero.health -= mobs.mob.attack()
            text.typetext(f"You tried to dodge, but failed. You have {character.Hero.health} health left.")
    elif Rsize == "small":
            if random.random() < 0.1 * character.Hero.agility:
                text.typetext(f"The {mobs.mob.name} attacked you, but you dodged.")
            else:
                character.Hero.health -= mobs.mob.attack()
                text.typetext(f"You tried to dodge, but failed. You have {character.Hero.health} health left.")
    elif Rsize == "huge":
            if random.random() < 0.3 * character.Hero.agility:
                text.typetext(f"The {mobs.mob.name} attacked you, but you dodged.")
            else:
                character.Hero.health -= mobs.mob.attack()
                text.typetext(f"You tried to dodge, but failed. You have {character.Hero.health} health left.")

def Tloot(Rtype):
    if Rtype == "Dining Hall":
        item = food.randomFood()
    elif Rtype == "Kitchen":
        item = food.randomFood()
    elif Rtype == "Storage Room":
        item = Items.randomItem()
    elif Rtype == "Assembly Hall":
        item = Items.randomItem()
    elif Rtype == "Library":
        item = Items.randomItem()
    hotkeys.inventory.append(item)
    return item