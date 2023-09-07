#INPUT
principal = int(input("Enter the principal: "))
interest_rate = float(input("Enter the interest rate: "))
frequency = int(input("Enter the compound frequency: "))
years = int(input("Enter the number of years: "))
#FUNCTION



new_principal = round(((interest_rate / (100 * frequency)) + 1) ** (frequency * years) * principal, 2)


#OUTPUT
print(f"${principal} invested at an interest rate of {interest_rate}% compounded {frequency} times annually will be worth ${new_principal} after {years} years.")
