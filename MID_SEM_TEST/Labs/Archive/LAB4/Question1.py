month = str(input("Enter the month: "))

if month == "September" or month == "October" or month == "November":
    print(f"{month} is in Spring.")
elif month == "December" or month == "January" or month == "February":
    print(f"{month} is in Summer.")
elif month == "March" or month == "April" or month == "May":
    print(f"{month} is in Autumn.")
elif month == "June" or month == "July" or month == "August":
    print(f"{month} is in Winter.")
else:
    print("Unknown month.")