# Prompt user to enter the starting, ending, and stepping values for a range.
num1 = int(input("Enter the start: "))
num2 = int(input("Enter the end: "))
step = int(input("Enter the step: "))

# Determine the actual start and end values based on user input.
start = min(num1, num2)
end = max(num1, num2)
number = start

# Iterate through the range and print each number separated by a space.
while number < end:
    print(f"{number} ", end="")
    number += step
