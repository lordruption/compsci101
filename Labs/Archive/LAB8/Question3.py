# Initialize an empty list to store modified characters.
new_chars = []

# Lists of uppercase and lowercase alphabet characters.
uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt the user to input text.
user_text = str(input("Please enter your text: "))

# Iterate through each character in the user's input.
# If the character is lowercase, convert it to uppercase and add it to the list.
# If the character is uppercase, convert it to lowercase and add it to the list.
# If the character is not an alphabet letter, keep it unchanged in the list.
for char in user_text:
    if char in lowercase_alpha:
        new_chars.append(char.upper())
    elif char in uppercase_alpha:
        new_chars.append(char.lower())
    else:
        new_chars.append(char)

# Join the modified characters to form a new string.
new_string = ''.join(new_chars)

# Display the modified text.
print("New text:", new_string)
