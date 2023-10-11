def get_sum_evens_odds(numbers_list):
    even = 0
    odd = 0
    for i in numbers_list:
        if i % 2 == 0:
            even = even + i
        elif i % 2 != 0:
            odd = odd + i
    return (even, odd)






numbers = [4, -5, 2, 8, 0, -4, ]
data = get_sum_evens_odds(numbers)
print(data)
print(type(data))