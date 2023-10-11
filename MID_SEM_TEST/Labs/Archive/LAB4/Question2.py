month = str(input("Enter the month: "))

if month == "January" or month == "March" or month == "May" or month == "July":
    print(f"{month} has 31 days.")
elif month == "August" or month == "October" or month == "December":
    print(f"{month} has 31 days.")
elif month == "February":
    print(f"{month} has 28 days.")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print(f"{month} has 30 days.")
else:
    print("Invalid month.")