import random
import os
import character
import stats
import hotkeys
import mobs

def clear():
    os.system('cls')


def choose_stats():
    Luck, Strength, Agility, Intelligence, Points = stats.stat()
    print("Before starting the game, define your character's attributes.\n You have 10 points that you can use to increase your stats.\n After that, you won't be able to change them.")
    print("Luck, Strength, Agility, Intelligence\n 10 Points\n")

    LuckS = int(input("Luck: "))
    Points -= LuckS

    StrengthS = int(input("Strength: "))
    Points -= StrengthS

    AgilityS = int(input("Agility: "))
    Points -= Agility
    
    IntelligenceS = int(input("Intelligence: "))
    Points -= Intelligence



def quest1():
    clear()
    print("\nYou encountered a Skeleton with a sword")
    skeleton = mobs.Skeleton.health
    while True:
        hotkeys.ui()
        do = input("\nAttack or Dodge?:").lower()

        if do == "attack":
            mobs.Skeleton.health -= character.Hero.damage
            
            if mobs.Skeleton.health > 0:
                clear()
                print(f"The skeleton has {mobs.Skeleton.health} health left")
                character.Hero.health -= mobs.Skeleton.damage
                print(f"The skeleton attacked you. You have {character.Hero.health} health left")
                
                if character.Hero.health <=0:
                    clear()
                    print("You have been defeated")
                    break
                    
            elif mobs.Skeleton.health <= 0:
                clear()
                print(f"The skeleton is defeated. You gained {mobs.Skeleton.XP} XP")
                character.Hero.XP += mobs.Skeleton.XP
                input("Continue the adventure. Press any key... ")
                clear()
                break
                
        elif do == "dodge":

            clear()
            if random.random() < 0.5:
                print("The skeleton attacked you, but you dodged.")
            else:
                character.Hero.health -= mobs.Skeleton.damage
                print(f"You tried to dodge, but failed. You have {character.Hero.health} health left.")
