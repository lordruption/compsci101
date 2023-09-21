alist = []
text = open('sentences.txt', "r")
textv1 = text.read().lower()
textv2 = textv1.split()
for word in textv2:
    if "s" in word[0]:
        alist.append(word)
    else:
        continue



print(alist)