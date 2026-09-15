import character
import text

#Function for character levels
def leveling():

    if character.Hero.XP == 100:

        character.Hero.level += 1
        character.Hero.health += 5
        text.typetext(f"You gained {character.Hero.level} level!")
        
    elif character.Hero.XP == 200:

        character.Hero.level += 1
        character.Hero.health += 5
        text.typetext(f"You gained {character.Hero.level} level!")

    elif character.Hero.XP == 300:

        character.Hero.level += 1
        character.Hero.health +=5
        text.typetext(f"You gained {character.Hero.level} level!")
