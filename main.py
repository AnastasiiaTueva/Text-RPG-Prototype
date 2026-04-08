import random
import os
import Events
import hotkeys
import stats

text = hotkeys.ui()

def clear():
    os.system('cls')


while True:
    clear()
    stats.beginning()
    clear()
    Quest = input("You take an item into your inventory. The elder leads you to the entrance of the dungeon.\n"
    "The end of this story lies entirely in your hands. Are you ready? (Yes, No): ").lower()
    if Quest == "no":
        print("\nEveryone got scared and left, and you stayed alone :(")
        break
    elif Quest == "yes":
        Events.quest1()
        
    else:
        print("\n0-0")
        break
