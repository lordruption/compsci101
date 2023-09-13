def check_palindrome(a_string):
    list = []
    a_string = a_string.lower()
    for i in a_string:
        if i.isalpha():
            list.append(i)
    reverse_list = list[::-1]
    if list == reverse_list:
        return True
    else:
        return False





	
a_string = "Madam, I'm Adam."
if check_palindrome(a_string):
    print("'", a_string, "' is a palindrome", sep="")
else:
    print("'", a_string, "' is not a palindrome", sep="")