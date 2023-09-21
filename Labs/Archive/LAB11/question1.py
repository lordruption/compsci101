def to_the_power_of(number, power):
    answer = number ** power
    return answer

number = int(input("Number: "))
power = int(input("Power: "))

result = to_the_power_of(number, power)
print(f"{number} to the power of {power} is {result}")
