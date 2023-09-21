list_of_number = []

user_input = input("Enter an integer number (blank to exit): ")

while user_input != "":
    user_num = int(user_input)
    list_of_number.append(user_num)
    user_input = input("Enter an integer number (blank to exit): ")

print(list_of_number)


