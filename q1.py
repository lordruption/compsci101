def duplicate_evens(numbers_list):
    # Loop through the list elements backwards
    for i in range(len(numbers_list) - 1, -1, -1):
        # Check if the current number is even
        if numbers_list[i] % 2 == 0:
            # Duplicate the even number by inserting it after its current position
            numbers_list.insert(i+1, numbers_list[i])
            
    









numbers = [1, 2, 3, 4, 5]
duplicate_evens(numbers)
print(numbers)