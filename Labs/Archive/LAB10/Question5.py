def is_valid_password(password):
    #remove any leading and trailing white space from the password
    strip_user_password = password.strip()
    #The password should have a length of at least 8 characters.
    #The first character of the password must be an alphabetical letter.
    #The password should have at least 4 alphabetical characters.
    #The password should have at least 3 numerical characters.

    strip_user_password_alpha = ""
    for char in strip_user_password:
        if char.isalpha():
                strip_user_password_alpha += char
    strip_user_password_digits = ""
    for char in strip_user_password:
        if char.isdigit():
                strip_user_password_digits += char

    if len(strip_user_password) < 8:
        return(False)
    elif strip_user_password[0].isalpha() == False:
        return(False)
    elif len(strip_user_password_alpha) < 4:
        return(False)
    elif len(strip_user_password_digits) < 3:
        return(False)
    else:
        return(True)


password = "abcd123"
print(password, "is a valid password:", is_valid_password(password))


