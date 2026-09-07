import random
import os
import Events
import hotkeys
import stats
import difficulty

# Terminal cleaning
def clear():
    os.system('cls')

clear()

rooms = difficulty.difficult()

Events.event = 0

clear()

#call the start event function and select the path
stats.beginning()
stats.beginning_item()

Quest = input("You take an item into your inventory. The elder leads you to the entrance of the dungeon.\n"
"The end of this story lies entirely in your hands. Are you ready? (Yes, No): ").lower()

if Quest == "no":

    print("\nEveryone got scared and left, and you stayed alone :(")

elif Quest == "yes":

    while True:

        clear()

        if Events.event >= 0:
            Events.quest1(rooms)

            if Events.event >= rooms:
                print("You finished the game!")
                input("Press any key to finish the game...")
                break
            
    else:

        print("\n0-0")
