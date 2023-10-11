def remove_all_repeats(numbers_list):
    sorted_list = sorted(numbers_list)
    unique_list = []
    prev_num = None
    for i in sorted_list:
        if i != prev_num:
            unique_list.append(i)
        prev_num = i
    return unique_list

def remove_all_repeats(numbers_list):
    numbers_list.sort() 
    i = 0
    while i < len(numbers_list) - 1:
        if numbers_list[i] == numbers_list[i + 1]:
            del numbers_list[i + 1]
        else:
            i += 1





# [3, 67, 71, 88, 99]
numbers = [3, 71, 71, 3, 99, 3, 67, 88]
remove_all_repeats(numbers)
print(numbers)