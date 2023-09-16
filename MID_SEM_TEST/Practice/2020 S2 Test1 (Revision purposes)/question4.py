def is_between_and_even(test_value, low_value, high_value):
    if low_value <= test_value and test_value <= high_value and test_value % 2 == 0:
        return True
    else:
        return False




'''
print(is_between_and_even(23, 22, 24)) #False
print(is_between_and_even(22.0, 22.0, 24.5)) #True
print(is_between_and_even(21.99, 22.0, 24.5)) #False
'''
print(is_between_and_even(24, 22, 24)) # True
print(is_between_and_even(23.99, 22.0, 24)) # False
print(is_between_and_even(24.99, 22.0, 24)) # False