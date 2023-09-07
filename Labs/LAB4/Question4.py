#user_input
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
third_num = float(input("Enter the second number: "))
user_answer = float(input(f"{first_num} + {second_num} + {third_num} = "))
#computer_answer
computer_answer = first_num + second_num + third_num
#torrence of "equal or less than  0.001"
tolerance = 0.001
#function
if abs(user_answer - computer_answer) <= tolerance:
    print("Correct")
else:
    print("Incorrect")