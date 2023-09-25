def read_length_per_line(filename):
    open_file = open(filename, 'r')
    read = open_file.read()
    split = read.split('\n')
    return_list = []
    for sentence in split:
        count = len(sentence)
        return_list.append(count)
    open_file.close()
    return return_list





'''
first_sentence = split[0]
second_sentence = split[1]
first_count = len(first_sentence)
second_count = len(second_sentence)
'''






filename = 'names.txt'
print(read_length_per_line(filename))