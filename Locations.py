import random
import character

def locationGen():

    sizeRoom1 = "small"
    sizeRoom2 = "middle"
    sizeRoom3 = "huge"

    typeRoom1 = "Dining Hall"
    typeRoom2 = "Kitchen"
    typeRoom3 = "Storage Room"
    typeRoom4 = "Assembly Hall"
    typeRoom5 = "Library"

    sizeRoom = [sizeRoom1,sizeRoom2,sizeRoom3]
    typeRoom = [typeRoom1, typeRoom2, typeRoom3, typeRoom4, typeRoom5]

    random_size = random.choice(sizeRoom)
    random_type = random.choice(typeRoom)

    print(f"You are in {random_size} {random_type}")
    return