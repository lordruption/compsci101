def process_transactions(filename):
    file_open = open(filename, "r")
    file_read = file_open.read()
    text_list = file_read.split()
    name = None
    total_value = 0 
    for line in text_list:
        line_split = line.split(':')
        name = line_split[0]
        amount = line_split[1]
        if name is None:  # Check if name is not assigned (for the first line)
            name = line_split[0]
        if name == line_split[0]:  # Check if the names match
            amount = int(line_split[1])  # Convert amount to an integer
            total_value += amount  # Update the total value
        return (name, total_value)


filename = "Transactions1.txt"
transaction_data = process_transactions(filename)
if transaction_data[1] < 0:
    print(f"The sum of transactions for {transaction_data[0]} = -${transaction_data[1] * -1}")
else:
    print(f"The sum of transactions for {transaction_data[0]} = ${transaction_data[1]}")

#Alpha Version