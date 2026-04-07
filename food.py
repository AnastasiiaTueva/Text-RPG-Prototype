class Food:

    def __init__(self, name, description, heal, price):
        self.name = name
        self.description = description
        self.heal = heal
        self.price = price
    
    def __str__(self):
        return self.name

Apple = Food("apple","A juicy ripe apple", 5, 10)