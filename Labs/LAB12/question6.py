def upper_vowel(sentence):
    sentence_list_final = []
    sentence_list = []
    sentence_lower = sentence.lower()
    vowels = ['a', 'e', 'i' ,'o' ,'u']
    for letter in sentence_lower:
        sentence_list.append(letter)
    for i in sentence_list:
        if i in vowels:
            sentence_list_final.append(i.upper())
        else:
            sentence_list_final.append(i)
    sentence_list_final_formatted = ''.join(map(str,sentence_list_final))
    return sentence_list_final_formatted



print(upper_vowel("Mohammad"))
print(upper_vowel("World cup 2022"))