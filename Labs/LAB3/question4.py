numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
if denominator == 0:
    print("Result: Undefined") 
else:
    answer = round(numerator / denominator, 2)
    print(f"Result: {answer}")