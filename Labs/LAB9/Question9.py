#Initialize an empty list to store the HTML tag names.
tag_names = []

#Prompt the user to enter some text using an appropriate message.
text = ("<p>This is a paragraph!</p>")

#Read and store the user's input text.
for char in text:
    if char == "<":
        tag = True
    elif char == ">":
        tag = False
    while tag == True:
        tag_names.append(char)

    

print("List of HTML tags: ")