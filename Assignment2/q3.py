#Question 1 - This function reads filename.txt
def read_dictionary_file(filename):
    input_stream = open(filename, 'r', encoding='utf-8')
    #This function split file by new line
    read_file = input_stream.read().split('\n')
    input_stream.close()
    return read_file
#Question 2 - This function takes a string list then returns it in dictionary format
def get_maori_english_dictionary(contents):
    maori_english_dictionary = {}
    listcontent = list(contents)
    for item in listcontent:
        #This turns 'Waipuke - Flood' to 'Waipuke': 'Flood'
        split_item = item.split(" - ")
        key = split_item[0]
        value = split_item[-1]
        maori_english_dictionary[key] = value
    return maori_english_dictionary
#Question 3 - This function prints dictionary in a proper format
def main():
    filename = "SampleDictionary1.txt" #do not change this line!
    contents = read_dictionary_file(filename)
    maori_english_dictionary = get_maori_english_dictionary(contents)
    list_maori_english_dictionary = list(maori_english_dictionary.keys())
    list_maori_english_dictionary.sort()
    sorted_list_maori_english_dictionary = {i: maori_english_dictionary[i] for i in list_maori_english_dictionary}
    for key, value in sorted_list_maori_english_dictionary.items():
        print(key + ":")
        print('   ' + value)


main()