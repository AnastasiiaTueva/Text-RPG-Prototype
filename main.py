import random
import os
import Events



def clear():
    os.system('cls')


while True:
    clear()
    Quest = input("Monsters have started coming out of a nearby dungeon and are scaring our village. Can you help us? :'( (Yes, No): ").lower()
    if Quest == "no":
        print("\nEveryone got scared and left, and you stayed alone :(")
        break
    elif Quest == "yes":
        Events.quest1()
    else:
        print("\n0-0")
        break