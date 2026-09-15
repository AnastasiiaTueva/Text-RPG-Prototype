import random
import os
import character
import stats
import hotkeys
import mobs
import Items
import Locations
import food
import text
import rooms
import level


def clear():
    os.system('cls')

#Variables for events, coins, and whether a merchant event is active.
event = 0
coins = 0
merchant = False

#Function for the recurring quest.
def quest1(mobH, Rtype):

    global event
    global coins
    clear()

    # Spawn random Monster
    mob = mobs.randomMob()
    mob.health = mob.health * (mobH // 5)

    Rsize, Rtype = Locations.locationGen()
    text.typetext(f"You encountered {mob.name}")

    #Merchant event and food purchasing.
    if event == 3 and not merchant:
        clear()

        text.typetext(f"You encountered a wandering merchant:\n" \
        f"You have {coins} coins")
        text.typetext("What do you want to buy?\n" \
        "Apple - 2 coins\n" \
        "Bread - 3 coins\n")
        buying = input("(Apple/Bread/No): ").lower()

        if buying == "apple" and coins >= 2:
            hotkeys.inventory.append(food.apple)
            input("You bought an Apple!")
            clear()
        elif buying == "bread" and coins >= 3:
            hotkeys.inventory.append(food.bread)
            input("You bought a Bread!")
            clear()
        else:
            input("You entered the command incorrectly. Press any key to continue.")
            clear()


    while True:
        # Creating the fight and results
        hotkeys.ui()
        do = input("\nAttack or Dodge?(A/D):").lower()

        if do == "a":
            if mob.health > 0:
                clear()

                mob.health -= character.Hero.attack()
                text.typetext(f"The {mob.name} has {mob.health} health left")

                if mob.health <= 0:
                    clear()

                    #Function for spawning a random item or food
                    item = rooms.Tloot(Rtype)
                    
                    text.typetext(f"The {mob.name} is defeated. You gained {mob.XP} XP. You got a {item.name}.")
                    character.Hero.XP += mob.XP
                    event += 1
                    coins += 1
                    text.typetext(f"finished event(s): {event}")

                    #Checking Exp and allowing the player to level up
                    level.leveling()
                        
                    input("Press any key to continue...")

                    clear()

                    break

                character.Hero.health -= mob.attack()
                text.typetext(f"The {mob.name} attacked you. You have {character.Hero.health} health left")
      
                if character.Hero.health <=0:
                    text.typetext("You have been defeated")
                    input("Press any key to continue...")

                    clear()

                    exit()

        #If-else functions for managing the inventory and statistics.
        elif do == "d":
            clear()

            rooms.Dsize()
            
        
        elif do == "i":
            hotkeys.I()
        
        elif do == "s":
            hotkeys.S()

        elif do == "x":
            break

        else:
            input("You entered the command incorrectly. Press any key to continue.")
            
            clear()
