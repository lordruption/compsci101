def get_user_selection():
    while True:
        selection = input("Enter your selection (1 to 5): ")
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= 5:
                return selection  # Returns the user's valid selection (an integer from 1 to 5)
        print("Please enter a number from 1 to 5")

def play_round(question_items, question_index):
    # Extract the target word and its corresponding value from the question_items list.
    maori_word = question_items[question_index][0]  # This is the target word
    maori_answer = question_items[question_index][1]  # This is the target value

    # Print a prompt to select the definition for the target word.
    print(f"Select the definition for the word {maori_word}")
    print()
    print("Choose from one of the following options:")
    print()

    title = 1
    # Iterate through the question_items list and display options along with their titles.
    for tuple in question_items:
        print(f"{title}) {tuple[1]}")
        title += 1
    print()

    remaining_attempt = 3  # Count the number of attempts allowed

    while remaining_attempt < 0:
        # Call the get_user_selection function to get the user's choice.
        selection = get_user_selection()

        correct_answer = question_index + 1  # Calculate the correct answer based on the question_index.

        # Check if the user's selection matches the correct answer.
        while selection != correct_answer:
            print("Your answer is incorrect.")
            remaining_attempt = remaining_attempt - 1
            print(f"You have {remaining_attempt} attempt(s) left. Please try again.")
            selection = get_user_selection()
        else:
            # Print a success message when the user provides the correct answer.
            print(f"Congratulations! {maori_word} does mean {maori_answer}!")
            print()
            break  # Exit the outer loop after a correct answer

    if remaining_attempt <= 0:
        # Display a message if the user runs out of attempts without providing the correct answer.
        print(f"You have not identified the meaning of {maori_word}")
        print(f"{maori_word} means {maori_answer}")
        print("Better luck next time!")

# TestCase
question_items = [('Repo', 'Swamp'), ('Turi', 'Knee'), ('Kiriata', 'Cinema'), ('Kai', 'Food'), ('Pune', 'Spoon')]
question_index = 4
print("Round score:", play_round(question_items, question_index))