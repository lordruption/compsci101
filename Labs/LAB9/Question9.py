#Initialize an empty list to store the HTML tag names.
tag_names = []

#Prompt the user to enter some text using an appropriate message.
text = input("Enter your text: ")

#Read and store the user's input text.
for char in text:
    if char == "<":
        tag = True
    elif char == ">":
        tag = True

print("List of HTML tags: ")