#This function Takes input, reprompts if no valid
def get_user_selection():
    #User Prompt
    user_selection = input("Enter your selection (1 to 5): ")
    while user_selection.isdigit() == False:
        print("Please enter a number from 1 to 5")
        user_selection = input("Enter your selection (1 to 5): ")
    
    while user_selection not in range(1, 6):
        print("Please enter a number from 1 to 5")
        user_selection = int(input("Enter your selection (1 to 5): "))

    return(user_selection)

print(get_user_selection())
