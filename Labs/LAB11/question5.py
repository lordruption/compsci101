def upper_vowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence_list = []
    lower_sentence = sentence.lower()
    for letter in lower_sentence:
        if letter in vowels:
            upper_letter = letter.upper()
            sentence_list.append(upper_letter)
        else:
            sentence_list.append(letter)
    return("".join(sentence_list))
