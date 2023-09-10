list = []

text = "<p>This is a paragraph!</p>"

tag = False  # Initialize the tag variable outside the loop

for letter in text:
    if letter == "<":
        tag = True
        current_tag = ""  # Initialize a variable to store the current tag
    elif letter == ">":
        tag = False
        list.append(current_tag)  # Append the current_tag to the list
    if tag == True:
        current_tag += letter  # Build the current tag character by character

print(list)
