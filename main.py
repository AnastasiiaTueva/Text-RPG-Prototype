import random
import os
import Events
import hotkeys
import stats

# Terminal cleaning
def clear():
    os.system('cls')


while True:

    clear()

    #call the start event function and select the path
    stats.beginning()
    stats.beginning_item()

    clear()

    Quest = input("You take an item into your inventory. The elder leads you to the entrance of the dungeon.\n"
    "The end of this story lies entirely in your hands. Are you ready? (Yes, No): ").lower()

    if Quest == "no":

        print("\nEveryone got scared and left, and you stayed alone :(")
        break
    
    #calling event functions (requires creating several events and their randomizer)
    elif Quest == "yes":

        Events.quest1()
        
    else:

        print("\n0-0")
        break
