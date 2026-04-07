import random
import os
import character
import stats
import hotkeys
import mobs
import Items

def clear():
    os.system('cls')

def quest1():
    clear()
    print("\nYou encountered a Skeleton with a sword")
    while True:
        hotkeys.ui()
        do = input("\nAttack or Dodge?:").lower()

        if do == "attack":
            mobs.Skeleton.health -= character.Hero.attack() + (character.Hero.strength // 2)
            
            if mobs.Skeleton.health > 0:
                clear()
                print(f"The skeleton has {mobs.Skeleton.health} health left")
                character.Hero.health -= mobs.Skeleton.attack()
                print(f"The skeleton attacked you. You have {character.Hero.health} health left")
                
                if character.Hero.health <=0:
                    clear()
                    print("You have been defeated")
                    break
                    
            elif mobs.Skeleton.health <= 0:
                clear()
                print(f"The skeleton is defeated. You gained {mobs.Skeleton.XP} XP. You got a Bone.")
                hotkeys.inventory.append("Bone")
                character.Hero.XP += mobs.Skeleton.XP
                input("Continue the adventure. Press any key... ")
                clear()
                break
                
        elif do == "dodge":

            clear()
            if random.random() < 0.2 * character.Hero.agility:
                print("The skeleton attacked you, but you dodged.")
            else:
                character.Hero.health -= mobs.Skeleton.attack()
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
