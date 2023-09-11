def is_valid_day():
    user_input = input("Enter your birth date (yyyy-mm-dd): ")
    month = user_input[5:7]
    day = user_input[8:10]
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "12":
        if day <= "31":
            return True
        else: 
            return False
    elif month == "02":
        if day <= "29":
            return True
        else: 
            return False
    else:
        if day <= "30":
            return True
        else: 
            return False
        












#January, March, May, July, August, October, December: 31 days.
#February: 29 days (we consider a leap year for all cases).
#April, June, September, November: 30 days.


print(is_valid_day())
