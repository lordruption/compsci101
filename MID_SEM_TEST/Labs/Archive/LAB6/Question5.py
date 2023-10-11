#vowels_lisk
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_in_word = []
#input
word = str(input("Enter a word: "))
lower_word = word.lower()

for char in lower_word:
    if char in vowels:
        vowels_in_word.append(char)
number_vowels_in_word = len(vowels_in_word)


print(f"{number_vowels_in_word} vowels.")