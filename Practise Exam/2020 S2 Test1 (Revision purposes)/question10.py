def word_puzzle(horizontal_str, vertical_str):
    vertical_str_list = list(vertical_str)
    horizontal_str_list = list(horizontal_str)
    common_letter = None
    for letter in horizontal_str:
        if letter in vertical_str:
            common_letter = letter
            break
    if common_letter == None:
        print("The two strings do not intersect.")
    vertical_str_index = vertical_str.find(common_letter)
    horizontal_str_index = horizontal_str.find(common_letter)
    for i in range(len(vertical_str)):
        if i == vertical_str_index:
            print(horizontal_str)
        else:
            print(' ' * horizontal_str_index + vertical_str[i])




word_puzzle("zero","match")
