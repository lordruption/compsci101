def filter_positive_list(raw_data):
    postive_numbers = []
    for num in raw_data:
        if num > 0:
            postive_numbers.append(num)
    raw_data.clear()
    raw_data.extend(postive_numbers)
    return postive_numbers





data = [-3, -2, -1, 0, 1, 2, 3]
filter_positive_list(data)
print(data)