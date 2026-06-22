import Events
import Items
import food
import character
import stats
import special


# Hotcase menu appearance
def ui():
    width = 60


    print("\n " + "-" * width + " ")

    menu = "(I) - Inventory | (S) - Stats | (X) - Exit"
    print("|" + menu.center(width) + "|")
    print(" " + "-" * width + " ")


# Creating an inventory list
inventory = []
inventory.append(food.Apple)


# Creating functionality for the letter I
def I():
    Events.clear()
    print("Inventory:")
    for item in inventory:
        print(f"{item}")

    choice = input("What item do you want to use?(object/No) ").lower()

    if choice.lower() == "no":
        return
    

    # Reaction to the fact that an item must be of the food class to restore health
    for item in inventory:
        if item.name.lower() == choice:
            if isinstance(item, food.Food):
                character.Hero.health += item.heal

            inventory.remove(item)
            print(f"{item.description} was used. Your current health {character.Hero.health}")
            return
    print("There is no such item")


# Creating functionality for the letter S
def S():
    print(f" Stats: Luck: {character.Hero.luck}, Strength: {character.Hero.strength}, Agility: {character.Hero.agility}, Intelligence: {character.Hero.intelligence}")
    print(f"ability: {special.Perk}. {special.Perk.description}")
    input("Continue the adventure. Press any key... ")
    Events.clear()
    return
