import random

# Creating a food class and characteristics
class Food:

    def __init__(self, name, description, heal, price):
        self.name = name
        self.description = description
        self.heal = heal
        self.price = price
    
    def __str__(self):
        return self.name


# Creating a food objects

def randomFood():

    foods = [
            Food("Apple", "A juicy ripe apple", 5, 10),
            Food("Bread", "A simple fresh bread", 8, 15),
    ]
    
    return random.choice(foods)
