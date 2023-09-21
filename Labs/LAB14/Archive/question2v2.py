def read_lines(filename):
    text = open(filename, "r")
    textv1 = text.read()
    textv2 = textv1.split('\n')
    return textv2
    textv2.close()






print(read_lines('sample_books.txt'))
