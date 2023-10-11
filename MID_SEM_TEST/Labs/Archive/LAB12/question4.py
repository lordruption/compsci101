import math 

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
sum = first_num + second_num
if math.sqrt(sum) % 1 != 0:
    print(f"The sum of {first_num} and {second_num} is not a square number.")
else:
    print(f"The sum of {first_num} and {second_num} is a square number.")
