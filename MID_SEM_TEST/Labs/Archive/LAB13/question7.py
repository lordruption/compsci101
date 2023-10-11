def word_analysis(word):
    letter_split_list = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word_length = len(word)
    score = 0
    for letter in word:
        letter_split_list.append(letter)
    for i in letter_split_list:
        score = score + letters.index(i)
    final = (word,word_length, score)
    return final




print(word_analysis('case'))
