import character

def choose_stats():
    
    print("Before starting the game, define your character's attributes.\n You have points that you can use to increase your stats.\n After that, you won't be able to change them.")
    print("Luck, Strength, Agility, Intelligence\n")

    Luck = int(input("Luck: "))
    character.Hero.luck += Luck

    Strength = int(input("Strength: "))
    character.Hero.strength += Strength

    Agility = int(input("Agility: "))
    character.Hero.agility += Agility
    
    Intelligence = int(input("Intelligence: "))
    character.Hero.intelligence += Intelligence
