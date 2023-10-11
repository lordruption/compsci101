def is_valid_day():
    user_input = input("Enter your birth date (yyyy-mm-dd): ")
    month = int(user_input[5:7])
    day = int(user_input[8:10])
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            return("False")
        else:
            return("True")
    elif month == 2:
        if day > 29:
            return("False")
        else:
            return("True")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return ("False")
        else:
            return("True")       


print(is_valid_day())