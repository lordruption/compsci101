#This function reads filename.txt
def read_dictionary_file(filename):
    input_stream = open(filename, 'r', encoding='utf-8')
    #This function split file by new line
    read_file = input_stream.read().split('\n')
    input_stream.close()
    return read_file

print(read_dictionary_file("SampleDictionary1.txt"))