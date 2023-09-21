# List for Alpha
lowercase_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# User text
user_text = input("Please enter your text: ")

# List to store transformed characters
new_chars = []

# Transformation Loop
for char in user_text:
    if char in lowercase_alpha:
        new_chars.append(char.upper())
    elif char in uppercase_alpha:
        new_chars.append(char.lower())
    else:
        new_chars.append(char)

# Building the new string
new_string = ''.join(new_chars)

# Printing the result
print("Transformed string:", new_string)
