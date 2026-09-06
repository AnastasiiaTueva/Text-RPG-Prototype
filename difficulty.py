def difficult():

    difficulty_choice = input("Select difficulty(easy, hard, hardcore):").lower()
    easy = "easy"
    hard = "hard"
    hardcore = "hardcore"
    match difficulty_choice:

        case "easy":
            return 1

        case "hard":
            return 1.5

        case "hardcore":
            return 2

def difficult_rooms():

    difficulty_choice = input("Select difficulty(easy, hard, hardcore):").lower()

    match difficulty_choice:

        case "easy":
            return 5

        case "hard":
            return 10

        case "hardcore":
            return 15
