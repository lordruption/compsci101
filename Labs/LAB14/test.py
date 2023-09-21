list = ['a|#', 'b|#', 'c|#', 'd|#', 'e|###', 'f|#', 'g|#', 'h|##', 'i|#', 'j|#', 'k|#', 'l|#', 'm|#', 'n|#', 'o|####', 'p|#', 'q|#', 'r|##', 's|#', 't|##', 'u|##', 'v|#', 'w|#', 'x|#', 'y|#', 'z|#']
alist = []
for word in list:
    count = 0
    for char in word:
        if char == "#":
            count = count + 1
            alist.append((word[0],count))
        else:
            continue
print(alist)

