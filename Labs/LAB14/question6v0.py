def process_transactions(filename):
    text_open = open(filename, "r")
    text_read = text_open.read()
    print(text_read)










filename = "Transactions1.txt"
'''
transaction_data = process_transactions(filename)
if transaction_data[1] < 0:
    print(f"The sum of transactions for {transaction_data[0]} = -${transaction_data[1] * -1}")
else:
    print(f"The sum of transactions for {transaction_data[0]} = ${transaction_data[1]}")
'''
