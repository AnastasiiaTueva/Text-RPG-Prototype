import random

# Creating a food class and characteristics
class Food:

    def __init__(self, name, description, heal):
        self.name = name
        self.description = description
        self.heal = heal
    
    def __str__(self):
        return self.name


# Creating a food objects

apple = Food("Apple", "A juicy ripe apple", 10)
bread = Food("Bread", "A simple fresh bread", 12)

def randomFood():

    foods = [apple, bread]
    
    return random.choice(foods)
