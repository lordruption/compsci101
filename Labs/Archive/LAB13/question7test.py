def word_analysis(word):
    user_list = []
    result_list = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word_length = len(word)
    for letter in word:
        user_list.append(letter)

    
    for i in user_list:
        index_location = letters.index(i)
        result_list.append(index_location)
    final = (word,word_length, result_list[1])
    return final










word = 'at'
print(word_analysis(word))