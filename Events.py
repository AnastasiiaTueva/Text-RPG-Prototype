import random
import os
import character

def clear():
    os.system('cls')

def quest1():
    print("\nYou encountered a Skeleton with a sword")
    skeleton = 20
    while True:
        
        Sdamage = random.randint(1,6)
        do = input("\nAttack or Dodge?:").lower()
        if do == "attack":
            skeleton = int(skeleton) - character.charDamage()
            
            if skeleton > 0:
                print(f"The skeleton has {skeleton} health left")
                health = character.charHealth() - Sdamage
                print(f"The skeleton attacked you. You have {health} health left")
                
                if health <=0:
                    clear()
                    print("You have been defeated")
                    break
                    
            elif skeleton <= 0:
                clear()
                print("The skeleton is defeated. You gained XP")
                input("Continue the adventure. Press any key... ")
                clear()
                break
                
        elif do == "dodge":
            print("The skeleton attacked you, but you dodged.")