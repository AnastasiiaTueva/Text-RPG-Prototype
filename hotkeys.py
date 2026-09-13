import Events
import Items
import food
import character
import stats
import special
import text

# Hotcase menu appearance
def ui():
    width = 60

    print("\n " + "-" * width + " ")

    menu = "(I) - Inventory | (S) - Stats | (X) - Exit"
    print("|" + menu.center(width) + "|")
    print(" " + "-" * width + " ")

# Creating an inventory list
inventory = []

# Creating functionality for the letter I
def I():
    Events.clear()
    text.typetext("Inventory:")
    for item in inventory:
        text.typetext(f"{item.name}")

    choice = input("What item do you want to use?(object/No) ").lower()

    if choice.lower() == "no":
        return
    

    # Reaction to the fact that an item must be of the food class to restore health
    for item in inventory:
        if isinstance(item, food.Food):
            if item.name.lower() == choice:
                character.Hero.health += item.heal

                inventory.remove(item)
                text.typetext(f"{item.description} was used. Your current health {character.Hero.health}")
                return
    text.typetext("There is no such item")


# Creating functionality for the letter S
def S():
    text.typetext(f"Exp: {character.Hero.XP}")
    text.typetext(f" Stats: Luck: {character.Hero.luck}, Strength: {character.Hero.strength}, Agility: {character.Hero.agility}, Intelligence: {character.Hero.intelligence}")
    text.typetext(f"ability: {special.Perk}. {special.Perk.description}")
    input("Continue the adventure. Press any key... ")
    Events.clear()
    return
