# Get user input for the string and the letter
user_string = str(input("Enter the string: "))
user_letter = str(input("Enter the letter: "))

# Find the index of the first occurrence of the letter using find
index_first = user_string.find(user_letter)

# Find the index of the last occurrence of the letter using rfind
index_last = user_string.rfind(user_letter)

if index_first == -1 or index_last == -1:
    print(f"The letter {user_letter} does not appear in {user_string}.")
else:
    # Print the results
    print(f"The index of the first occurrence of {user_letter} in {user_string} is {index_first}.")
    print(f"The index of the last occurrence of {user_letter} in {user_string} is {index_last}.")

