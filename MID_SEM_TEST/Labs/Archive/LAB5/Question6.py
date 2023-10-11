total = 0
number_of_inputs = 0

user_num = float(input("Enter a number: "))

if user_num < 0:
        print("Average: undefined") 
else:
    while 0 < user_num:
        number_of_inputs = number_of_inputs + 1
        total = total + user_num
        user_num = float(input("Enter a number: ")) 
    if user_num <= 0:
        average = total / number_of_inputs
        if average < 0:
            print("Average: undefined")
        else:
            print(f"Average: {average}")