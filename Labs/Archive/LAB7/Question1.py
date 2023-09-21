#empty list
secret_message_list = []
#user input
code = str(input("Please enter the code: "))
#add user input to list
secret_message_list = list(code)
# Find the index of the first occurrence of the letter using find
index_first = code.find("(")
index_first_corrected = index_first + 1
# Find the index of the last occurrence of the letter using rfind
index_last = code.rfind(")")

message = secret_message_list[index_first_corrected:index_last]

for string in message:
    concatenated_string = concatenated_string = ''.join(message)

if index_first == -1 or index_last == -1:
    print("No secret message!")
else:
    print(f"Secret message: {concatenated_string}")