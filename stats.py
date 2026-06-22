import character
import Events
import hotkeys
import os
import special

# Terminal cleaning
def clear():
    os.system('cls')


# The start event function and select the path
def beginning():
    clear()
    print("Stranger! I know this is a sudden, but we need your help.\n" \
    "Our dungeon has been overrun by monsters, and recently they have started raiding our village\n" \
    "Can you destroy the monsters and reclaim the dungeon for us?\n\n")
    begin = input(" - Can you tell me more about the dungeon?(Intelligence route) (1)\n" \
                  
    " - How strong are the monsters in the dungeon?(Strength route) (2)\n" \
    " - Are there any traps in the dungeon? (Agility route) (3)\n" \
    " - Are there treasures in the dungeon? (Luck route) (4)\n" \
    "Choose the question(1,2,3,4): ")

    if begin == "1":
        clear()
        character.Hero.intelligence += 5
        special.Perk = special.SurvivalSense
        print(" Before the monsters came, we used the dungeon for feasts. Many joyful events in our settlement were celebrated there.\n" \
        "But because of the monster raids, we had to abandon it. There may still be food and drink left inside.\n")
        print("You got Survival Sense.")
        input("Continue the adventure. Press any key... ")

    elif begin == "2":
        clear()
        character.Hero.strength += 5
        special.Perk = special.CombatInsight
        print("Most of the raids are carried out by skeletons and slimes.\n"
           "They are not particuarly dangerous and are quite slow.\n" \
        " With a good strike, you can easily stun a skeleton and finish it off, and slimes can simply be burned.\n" \
        " However we fear monsters may also dwell there.")
        print("You got Combat insight\n")
        input("Continue the adventure. Press any key... ")

    elif begin == "3":
        clear()
        character.Hero.agility += 5
        special.Perk = special.TrapSense
        print("Now that you mention it, I recall some rumors \n" \
        "Someone exploring the dungeon once claimed that certain pieces of furniture were moving on their own...\n" \
        "though I am not sure how true that is.")
        print("You got Trap Sense\n")
        input("Continue the adventure. Press any key... ")

    elif begin == "4":
        clear()
        character.Hero.luck += 5
        special.Perk = special.WeirdLuck
        print("We had to leave dungeon in a hurry, and many villagers' belongings were left behind.\n " \
        "You may use them if you wish, but i would be grateful if you return them to their owners afterward.")
        print("You got Weird Luck\n")
        input("Continue the adventure. Press any key... ")

    else:
        clear()
        print("Choose a number(1,2,3,4).\n ")
        input("Continue the adventure. Press any key... ")
        return
    clear()

# Function to get the first item
def beginning_item():
    print("Our settlement is not wealthy, but you may take any item from our storage.\n" \
    "(You head to the local storage with the village elder.\n" \
    "It is a small wooden, hut, filled with the smell of dust and tree sap.\n" \
    "The hut is cluttered with various household tools, though few seem useful for your journey.)\n")
    print(" Stick - A smooth handle for future axe, pickaxe, or something similar.\n " \
    "Doesn't sound very useful, but with enough imagination, it might prove handy.\n\n" \
    " Rope - A three-meter length of rope. It looks almost unused, as if someone placed it here recently.\n" \
    "With the right skill, it could be very useful\n\n" \
    " Dagger - A small silver dagger. It looks worn, but still usable. Compared to your iron sword,\n" \
    "it may not seem like a great option, but it could give you an advantage against enemies.\n\n" \
    " Horseshoe - Looks very well crafted. likely made by a renowned blacksmith.\n" \
    "It may not seem useful, but if you are superstitious, it might bring you a bit of luck.\n\n")
    startItem = input("Which item will you take?(Stick, Rope, Dagger, Horseshoe): ").lower()
    if startItem == "stick":
        hotkeys.inventory.append("Stick")
    elif startItem == "rope":
        hotkeys.inventory.append("Rope")
    elif startItem == "dagger":
        hotkeys.inventory.append("Dagger")
    elif startItem == "horseshoe":
        hotkeys.inventory.append("Horseshoe")
    else:
        clear()
        print("Choose an item(Stick, Rope, Dagger, Horseshoe).")
        input("Continue the adventure. Press any key... ")
        return
