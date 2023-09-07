#user_input
n = int(input("Enter a number: "))
#initialization
factor = 2
#function
if n < 2:
        print("No prime factors")
else:
    print(f"The prime factors of {n} are:")
while factor <= n:
    if n % factor == 0:
        print(factor)
        n = n / factor
    else:
        factor = factor + 1

