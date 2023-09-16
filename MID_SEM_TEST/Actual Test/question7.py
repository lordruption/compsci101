def count_strings(list_of_strings, letter):
    counter = 1
    for i in data:
        if letter in list_of_strings[i]:
            counter = counter + 1
        return(counter)















data = ["Granny Smith Apple", "Bosc Pear", "Manzano Banana", "Blood Orange", "Red Grape", "Stella Cherry"]
print(count_strings(data, 'a'))
