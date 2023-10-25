def pop_and_append(numbers_list):
    indexcount = 0 
    for i in numbers_list:
        if i == indexcount:
            numbers_list.remove(i)
        else:
            indexcount += 1
            
            
    







numbers_list = [8, 4, 9, 3, 9, 1, 4, 0, 6, 1]
pop_and_append(numbers_list)
print(numbers_list)