import random
import os
import character
import stats
import hotkeys
import mobs
import Items
import Locations
import food

def clear():
    os.system('cls')

event = 0
coins = 0

def quest1(mobH):

    global event
    global coins
    clear()
    
    # Create random location
    Locations.locationGen()

    foods = food.randomFood()

    # Spawn random Monster
    mob = mobs.randomMob()

    mob.health = mob.health * (mobH // 5)

    print(f"You encountered {mob.name}")

    
    while True:
        # Creating the fight and results
        hotkeys.ui()
        do = input("\nAttack or Dodge?(A/D):").lower()

        if do == "a":
            
            if mob.health > 0:
                clear()

                mob.health -= character.Hero.attack()
                print(f"The {mob.name} has {mob.health} health left")

                if mob.health <= 0:
                    clear()
                    print(f"The {mob.name} is defeated. You gained {mob.XP} XP. You got a {foods.name}.")
                    hotkeys.inventory.append(foods)
                    character.Hero.XP += mob.XP
                    event += 1
                    coins += 1
                    print(f"finished event(s): {event}")
                    input("Press any key to continue...")
                    clear()
                    break

                character.Hero.health -= mob.attack()
                print(f"The {mob.name} attacked you. You have {character.Hero.health} health left")
      
                if character.Hero.health <=0:
                    
                    print("You have been defeated")
                    input("Press any key to continue...")
                    clear()
                    exit()

                if event == 3:
                    print(f"You encountered a wandering merchant:\n" \
                    f"You have {coins} coins")
                    print("What do you want to buy?\n" \
                    "Apple - 2 coins\n" \
                    "Bread - 3 coins\n")
                    buying = input("(Apple/Bread/No): ").lower()
                    if buying == "apple" and coins >= 2:
                        hotkeys.inventory.append(foods.apple)
                    elif buying == "bread" and coins >= 3:
                        hotkeys.inventory.append(foods.bread)
                    else:
                        input("You entered the command incorrectly. Press any key to continue.")
                        clear()
               
        elif do == "d":

            clear()
            if random.random() < 0.2 * character.Hero.agility:
                print(f"The {mob.name} attacked you, but you dodged.")
            else:
                character.Hero.health -= mob.attack()
                print(f"You tried to dodge, but failed. You have {character.Hero.health} health left.")
        
        elif do == "i":
            hotkeys.I()
        
        elif do == "s":
            hotkeys.S()

        elif do == "x":
            break

        else:
            input("You entered the command incorrectly. Press any key to continue.")
            clear()
