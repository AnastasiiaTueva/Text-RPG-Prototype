import random
import os
import Events
import hotkeys
import stats
import difficulty


rooms = difficulty.difficult()
Events.event = 0

# Terminal cleaning
def clear():
    os.system('cls')

difficulty.difficult()

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
            Events.quest1()

            if difficulty.difficult == "easy" and Events.event == 5:
                print("You finished the game!")
                input("Press any key to continue...")

            elif difficulty.difficult == "hard" and Events.event == 10:
                print("You finished the game!")
                input("Press any key to continue...")

            elif difficulty.difficult == "hardcore" and Events.event == 15:
                print("You finished the game!")
                input("Press any key to continue...")
            

        
        else:

            print("\n0-0")
            break
