number1 = int(input("Enter the start: "))
number2 = int(input("Enter the end: "))
step = int(input("Enter the step: "))
start = min(number1, number2)
end = max(number1, number2)
for number in range(start, end, step):
    print(f"{number} ", end="")