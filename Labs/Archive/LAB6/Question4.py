#input
user_word = str(input("Enter a word: "))
#reverse word
reverse_user_word = user_word[::-1]
if reverse_user_word == user_word:
    print(f"{user_word} is a palindrome.")
else: 
    print(f"{user_word} is not a palindrome.")
