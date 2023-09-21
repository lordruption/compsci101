def get_total(number):
    total = 0
    number_plus_one = number + 1 
    for i in range(0,number_plus_one):
        total = total + i
    return total


def create_tuples_list(number):
    list = []
    number_plus_one = number + 1 
    for i in range(0,number_plus_one):
        list.append((i,))
    return list


a_list = create_tuples_list(5)
print(a_list)
