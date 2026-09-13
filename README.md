Console Roguelike

---------------------------------------------------------------------------------------------------------------
A small text-based roguelike game written in Python.
---------------------------------------------------------------------------------------------------------------

This project was created as a personal programming project while i was learning Python. 
The main goal was to practice Python, object-oriented programming, random generation.

---------------------------------------------------------------------------------------------------------------
About the game
---------------------------------------------------------------------------------------------------------------

The player explores a randomly generated dungeon and encounters different monsters, locations, events, food and items.
Each room is generated with:
- A random size
- A random room type
The room size affects the chance of successfully dodging a monster's attack.
The room type affects the type of reward the player can receive after defeating a monster.

---------------------------------------------------------------------------------------------------------------
Features
---------------------------------------------------------------------------------------------------------------

- Character with health, XP, random damage and level
- Character abilities: Strength, Agility, Intelligence, Luck
- Randomly generated monsters
- Different monster characteristics
- Random room generation
- Different room sizes
- Different room types
- Combat system
- Dodge mechanic affected by Agility
- XP and leveling system
- Random food
- Food restores health
- Random items
- Inventory
- Player statistics
- Merchant event
- Simple console UI
- Animated text output

-------------------------------------------------------------------------------------------------------------------
Project structure
-------------------------------------------------------------------------------------------------------------------

import random.py         # Demo version of the game
Events.py                # Game events
Items.py                 # Item system
Locations.py             # Random location generation
Character.py             # Player character and character statistics
difficulty.py            # Difficulty selection
food.py                  # Food class and random food generation
hotkeys.py               # Inventory, statistic and interface
level.py                 # Leveling system
main.py                  # Main game loop
mobs.py                  # Monster class and random monster generation
rooms.py                 # Room and dodge logic
special.py               # Abilities
stats.py                 # Start event and selecting first item in inventory
text.py                  # Animated console text

---------------------------------------------------------------------------------------------------------------------
Author
---------------------------------------------------------------------------------------------------------------------
Created as a personal Python learning project.

Some parts of the project were developed with the help of AI when i encountered errors or needed help understanding a problem.
I tried to keep as much of my own code and decision-making as possible and use AI primarily as a debugging and learning tool.
The animated console text system was largely rewritten with AI assistance.
