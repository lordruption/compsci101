def make_palindrome(a_string):
    a_string = a_string.replace(" ", "")
    a_string = a_string.lower()
    a_string_list = []
    not_palindrome_answer = None
    for char in a_string:
        if char.isalpha() or char.isdigit() == True:
            a_string_list.extend(char)
        else:
            pass
    a_string_stripped = ''.join(a_string_list)
    if a_string_stripped != a_string_stripped[::-1]:
        not_palindrome_answer = a_string_stripped + a_string_stripped[::-1]
        return not_palindrome_answer
    elif a_string_stripped == a_string_stripped[::-1]:
        return a_string_stripped

    
a_string = "Damir"
print("The palindrome version of", a_string, "is", make_palindrome(a_string))
a_string = "Hello World123"
print("The palindrome version of", a_string, "is", make_palindrome(a_string))
a_string = "Madam I'm Adam"
print("The palindrome version of", a_string, "is", make_palindrome(a_string))