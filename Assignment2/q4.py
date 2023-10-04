#This function prints user's name and game instruction
def print_quiz_info(name):
    name_length = len(name)
    #This prints specific amount of * so that its the lenght of name
    print("*" * 33 + "*" * name_length)
    print(f"*Welcome {name} to the Reo Māori Quiz!*")
    print("*" * 33 + "*" * name_length)
    
    
    #Below is standard output DO NOT CHANGE
    print()
    print("The quiz has 5 rounds.")
    print("In each round you have to work out the English meaning of a Māori word.")
    print("You are given 5 options to select from and 3 attempts to select the right one.")
    print("Get the right answer and you score 1 point for the round.")
    print("Otherwise you score 0 points for the round.")
    print("Good luck!")





print_quiz_info("Ann")
