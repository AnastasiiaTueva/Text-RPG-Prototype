import random
import os
import Events
import hotkeys
import stats
import difficulty
import food
import rooms
import Locations

# Terminal cleaning
def clear():
    os.system('cls')

clear()

#Function for selecting the game difficulty
rooms = difficulty.difficult()

#Variable for counting the number of completed rooms.
Events.event = 0

clear()

#call the start event function and select the path
stats.beginning()

clear()

#Event function for obtaining the first item.
stats.beginning_item()

clear()

#Function for spawning random food and adding food to the player's inventory.
foods = food.randomFood()
hotkeys.inventory.append(foods)

#Start of the game loop.
Quest = input("You take an item into your inventory. The elder leads you to the entrance of the dungeon.\n"
"The end of this story lies entirely in your hands. Are you ready? (Yes, No): ").lower()

if Quest == "no":
    print("\nEveryone got scared and left, and you stayed alone :(")

elif Quest == "yes":
    while True:

        clear()

        #Function for creating a random room.
        Rsize, Rtype = Locations.locationGen()

        #Property: while the Event variable is greater than or equal to zero, the loop continues.
        if Events.event >= 0:
            Events.quest1(rooms, Rtype)

        #Property: as soon as the variable reaches the selected difficulty level, the game loop stops.
        if Events.event >= rooms:
            print("You finished the game!")
            input("Press any key to finish the game...")
            break
            
    else:

        print("\n0-0")
