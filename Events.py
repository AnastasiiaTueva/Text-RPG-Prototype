import random
import os
import character
import stats
import hotkeys
import mobs
import Items
import Locations
import food
import difficulty

def clear():
    os.system('cls')

event = 0
mobH = difficulty.difficult()

def quest1():

    global event
    global mobH
    clear()

    # Create random location
    Locations.locationGen()

    foods = food.randomFood()

    # Spawn random Monster
    mob = mobs.randomMob()

    mob.health = mob.health * mobH

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
                character.Hero.health -= mob.attack()
                print(f"The {mob.name} attacked you. You have {character.Hero.health} health left")
      
                if character.Hero.health <=0:
                    clear()
                    print("You have been defeated")
                    input("Press any key to continue...")
                    event -= 1
                    break
                    
            elif mob.health <= 0:
                clear()
                print(f"The {mob.name} is defeated. You gained {mob.XP} XP. You got a {foods.name}.")
                hotkeys.inventory.append(foods)
                character.Hero.XP += mob.XP
                event += 1
                print(f"finished event(s): {event}")
                input("Press any key to continue...")
                clear()
                break
               
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
