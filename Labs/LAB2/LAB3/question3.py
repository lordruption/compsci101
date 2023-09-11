first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
user_answer = int(input(f"Enter {first_num} * {second_num } = "))

if first_num * second_num == user_answer:
    print("Correct")
else:
    print("Incorrect")

