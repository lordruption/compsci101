def get_zero_ending_numbers_count(string_of_numbers):
    string_of_numbers = string_of_numbers.strip()
    string_of_numbers = string_of_numbers.split(' ')
    count = 0
    index = 0
    while index < len(string_of_numbers):
        if string_of_numbers[index][-1] == '0':
            count = count + 1
        index = index + 1
    return count




print(get_zero_ending_numbers_count("75 672 31 46 "))
print(get_zero_ending_numbers_count("100 0 340 "))
