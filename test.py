def multiply_nested_list_by_factors(nested_list, factors):
    new_list = []
    count = -1
    for sublist in nested_list:
        count = count + 1
        subsublist = []
        for number in sublist:
            answer = number * factors[count]
            subsublist.append(answer)
        new_list.append(subsublist)
    index = 0
    for number in nested_list:
        nested_list[index] = new_list[index]
        index = index + 1
    






nested_list = [[32, 3, 6], [-10, 20, 14], [42, -5, 41, 23, 18],
               [46, 30, 42, 10]]
factors = (9, 2, 9, -4)
multiply_nested_list_by_factors(nested_list, factors)
print(nested_list)
