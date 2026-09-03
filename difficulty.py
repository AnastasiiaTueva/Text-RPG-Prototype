def difficult():

    difficulty_choice = input("Select difficulty(easy, hard, hardcore):").lower()

    easy = 5
    hard = 10
    hardcore = 15
    match difficulty_choice:

        case "easy":
            
            return 1

        case "hard":

            return 1.5

        case "hardcore":

            return 2
