char_list = []
#user input
user_text = input("Enter your text: ")
#loop
for char in user_text:
    if char.isalpha():
        char_list.append(char)


list_complete = "".join(char_list)

print(list_complete)
