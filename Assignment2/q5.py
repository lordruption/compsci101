#This function takes user_selection but it to be in the range of 1 to 5
def get_user_selection():
    while True:
        selection = input("Enter your selection (1 to 5): ")
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= 5:
                return selection
        print("Please enter a number from 1 to 5")


print(get_user_selection())
