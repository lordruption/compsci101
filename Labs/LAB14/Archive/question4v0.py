def get_list_of_words_start_with(filename, target_letter):
    alist = []
    text = open(filename, "r")
    textv1 = text.read().lower()
    textv2 = textv1.split()
    for word in textv2:
        if target_letter in word[0]:
            alist.append(word)
        else:
            continue
    return alist

    


words_list = get_list_of_words_start_with("sentences.txt", 'a')
print(words_list)
