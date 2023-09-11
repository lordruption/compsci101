#input
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
user_answer = float(input(f"Enter {first_number} * {second_number} = "))
#function
computer_answer = first_number * second_number
#torrence of "equal or less than  0.001"
tolerance = 0.001
#loop
if abs(user_answer - computer_answer) <= tolerance:
    print("Correct")
else:
    print("Incorrect")

