#input
month = str(input("Enter the month: "))
year = int(input("Enter the year: "))
#function for year
if year % 400 == 0:
    leap_year = "yes"
elif year % 100 == 0:
    leap_year = "no"
elif year % 4 == 0:
    leap_year = "yes"
else:
    leap_year = "no"

#function for month
if leap_year == "yes":
    if month == "January" or month == "March" or month == "May" or month == "July":
        print(f"{month} has 31 days.")
    elif month == "August" or month == "October" or month == "December":
        print(f"{month} has 31 days.")
    elif month == "February":
        print(f"{month} has 29 days.")
    elif month == "April" or month == "June" or month == "September" or month == "November":
        print(f"{month} has 30 days.")
    else:
        print("Invalid month.")    
elif leap_year == "no":
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



