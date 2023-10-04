# This function takes input, reprompts if not valid
def get_user_selection():
    while True:
        user_input = input("Enter your selection (1 to 5): ")
        if user_input.isdigit():
            user_input_int = int(user_input)
            if user_input_int in range(1, 6):
                return user_input_int
        print("Please enter a number from 1 to 5")

print(get_user_selection())
