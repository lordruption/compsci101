import math
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
sum = first + second
sqrt_sum = math.sqrt(sum) 
if sqrt_sum % 1 == 0:
    print(f"The sum of {first} and {second} is a square number.")
else:
    print(f"The sum of {first} and {second} is not a square number.")



