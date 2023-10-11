# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the entered number is less than 2
if number < 2:
    print("No prime factors")  # If less than 2, it has no prime factors
else:
    print(f"The prime factors of {number} are:")
    factor = 2  # Start with the smallest prime factor

    # Iterate through potential factors from 2 to the entered number
    while factor <= number:
        if number % factor == 0:  # If the current factor divides the number
            print(factor)  # Print the factor, as it's a prime factor
            number //= factor  # Reduce the number by dividing it by the factor
        else:
            factor += 1  # Move to the next potential factor
