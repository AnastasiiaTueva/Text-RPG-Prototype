import random
import os
import character
import stats


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
    print("\nYou encountered a Skeleton with a sword")
    skeleton = 20
    while True:
        
        Sdamage = random.randint(1,2)
        do = input("\nAttack or Dodge?:").lower()
        if do == "attack":
            skeleton = int(skeleton) - character.Hero.damage
            
            if skeleton > 0:
                print(f"The skeleton has {skeleton} health left")
                character.Hero.health -= Sdamage
                print(f"The skeleton attacked you. You have {character.Hero.health} health left")
                
                if character.Hero.health <=0:
                    clear()
                    print("You have been defeated")
                    break
                    
            elif skeleton <= 0:
                clear()
                print("The skeleton is defeated. You gained 20 XP")
                character.Hero.XP += 20
                input("Continue the adventure. Press any key... ")
                clear()
                break
                
        elif do == "dodge":
            print("The skeleton attacked you, but you dodged.")
