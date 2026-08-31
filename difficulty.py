def difficult():

    difficulty_choice = input("Select difficulty(easy, hard, hardcore):").lower()

    easy = 5
    hard = 10
    hardcore = 15
    match difficulty_choice:

        case "easy":
            
            return easy

        case "hard":

            return hard

        case "hardcore":

            return hardcore