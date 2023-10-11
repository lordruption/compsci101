#This function takes user_selection but it to be in the range of 1 to 5
def get_user_selection():
    while True:
        selection = input("Enter your selection (1 to 5): ")
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= 5:
                return selection
        print("Please enter a number from 1 to 5")

#This function plays a single round of the Reo Māori Quiz
def play_round(question_items, question_index):
    attempts = 3
    target_word = question_items[question_index][0]
    target_key_int = int(question_index + 1)
    target_meaning = question_items[question_index][1]
    print(f"Select the definition for the word {target_word}")
    print()
    print("Choose from one of the following options:")
    print()
    iteration = 1
    for answer in question_items:
        print(f"{iteration}) {answer[1]}")
        iteration = iteration + 1
    print()
    while attempts > 0:
        user_selection = get_user_selection()
        attempts = attempts - 1
        if user_selection == target_key_int:
            print()
            print(f"Congratulations! {target_word} does mean '{target_meaning}'!")
            print()
            return 1
        else:
            print("Your answer is incorrect.")
            if attempts > 0:
                print(f"You have {attempts} attempt(s) left. Please try again.")
            print()
            continue
    else:
        print(f"You have not identified the meaning of {target_word}")
        print(f"{target_word} means '{target_meaning}'")
        print("Better luck next time!")
        print()
        return 0
            



#TestCase
question_items = [('Hui', 'Meeting'), ('Karanga', 'The ceremony of calling to the guests to welcome them onto the marae '),
                  ('Hereturi-kōkā', 'August '), ('Hōngongoi', 'July'), ('Kauae', 'Chin')]
question_index = 1
print("Round score:", play_round(question_items, question_index))
