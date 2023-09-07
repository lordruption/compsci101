# Initialize empty lists and counters
user_text_list = []  # List to store words from user's input text
target_word_list = []  # List to store words from target word
target_words_in_user_text_list = []  # List to store target words found in user's text
number_of_target = 0  # Counter for the number of times target word appears

# User input
user_text = str(input("Enter your text: "))  # Get user's input text
target_word_og = str(input("Enter the target word: "))  # Get the target word
target_word_og_og = target_word_og  # Store the original target word

# Convert input to lowercase
user_text = user_text.lower()  # Convert user's text to lowercase
target_word_og = target_word_og.lower()  # Convert target word to lowercase

# Split input text and target word into lists of words
user_text = user_text.split()  # Split user's text into a list of words
target_word_split = target_word_og.split()  # Split target word into a list of words

# Populate lists with words
for word in user_text:
    user_text_list.append(word)  # Add words from user's text to the list
for word in target_word_split:
    target_word_list.append(word)  # Add words from target word to the list

# Check for target words in user's text
for word in user_text_list:
    if word in target_word_list:
        target_words_in_user_text_list.append(word)  # Add target words found to the list
number_of_target = len(target_words_in_user_text_list)  # Count the number of target words found

# Output the result
if number_of_target == 1:
    print(f"The word '{target_word_og_og}' appears {number_of_target} time in the text.")
else:
    print(f"The word '{target_word_og_og}' appears {number_of_target} times in the text.")
