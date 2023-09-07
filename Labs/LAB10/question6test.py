def filter_positive_list(data):
    positive_integers = []
    for num in data:
        if isinstance(num, int) and num > 0:
            positive_integers.append(num)





data = [-3, -2, -1, 0, 1, 2, 3]
filter_positive_list(data)
print(data)