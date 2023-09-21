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
    beta_list = []
    for word in alist:
        if word not in beta_list:
            beta_list.append(word)
        else:
            continue
    return beta_list
    alist.close()

	
	
	
words_list = get_list_of_words_start_with("sentences.txt", 's')
print(words_list)