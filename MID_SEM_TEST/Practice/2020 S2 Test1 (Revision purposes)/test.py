def word_puzzle(horizontal_str, vertical_str):
    common_char = None
    for letter in horizontal_str:
        if letter in vertical_str:
            common_char = letter
            print_puzzle(common_char, vertical_str, horizontal_str)
            break
    if common_char == None:
        print("The two strings do not intersect")
def print_puzzle(common_char, vertical_str, horizontal_str):
    vertical_str_index = vertical_str.find(common_char)
    horizontal_str_index = horizontal_str.find(common_char)
    for i in range(len(vertical_str)):
        if i == vertical_str_index:
            print(horizontal_str)
        else:
            print(' ' * horizontal_str_index + vertical_str[i])


# Example usage:
word_puzzle("colony", "yummy")
