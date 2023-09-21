def process_transactions(filename):
    name = None
    total_value = 0
    accumulated_list = []
    for line in filename:
        line_split = line.split(':')
        name = line_split[0]
        amount = line_split[1]
        if name is None:  # Check if name is not assigned (for the first line)
            name = line_split[0]
        if name == line_split[0]:  # Check if the names match
            amount = int(line_split[1])  # Convert amount to an integer
            total_value += amount  # Update the total value
        return (name, total_value)


filename = ['Jennine:0', 'Abdelmoula:500', 'Ornella:-200', 'Jennine:-300', 'Abdelmoula:-150', 'Costinel:250', 'Jennine:427', 'Costinel:-90', 'Abdelmoula:-120', 'Costinel:107', 'Jennine:23', 'Ornella:139', 'Asad:67', 'Asad:23', 'Asad:100', 'Jennine:217']
transaction_data = process_transactions(filename)
print(transaction_data)


# In this version I will hard code the data in the program
