def get_starting_word():
    #returns a random word, all in uppercase characters.
def get_hidden_word(word):
    #returns a string which is the same as the word parameter except
    #that every alternate letter is replaced by a "_" character.
def get_user_guess(request, hidden_word):
    #Prints "The hidden word: " followed by the hidden_word parameter and 
    #then prompts the user to enter their guess using the request parameter
    #as the prompt. The function returns the string entered by the user in uppercase characters.
def get_number_incorrect(word, hidden_word, user_guess):
    #Returns the number of hidden letters which were incorrectly guessed by the user.
def print_feedback(word, user_guess, number_incorrect):
    #Prints a blank line followed by a line of feedback about the user guess.


random.seed(45) 
main()