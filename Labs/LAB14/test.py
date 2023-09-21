def process_transactions(filename):
    name = None
    total_amount = 0 
    text_open = open(filename, "r")
    text_read = text_open.read()
    text_list = text_read.split() 
    text_open.close()
    sorted_list = []
    for line in text_list:
        split = line.split(":")
        sorted_list.append(split)
    for line in sorted_list:
        name = line[0].strip()
        transaction_amount = int(line[1])
        if name == "Jennine":
            total_amount += transaction_amount
        else:
            continue
    return 





filename = "Transactions1.txt"
transaction_data = process_transactions(filename)
if transaction_data[1] < 0:
    print(f"The sum of transactions for {transaction_data[0]} = -${transaction_data[1] * -1}")
else:
    print(f"The sum of transactions for {transaction_data[0]} = ${transaction_data[1]}")
#Output: The sum of transactions for Jennine = $367
