def process_transactions(filename):
    file_open = open(filename, "r")
    file_read = file_open.read()
    text_list = file_read.split()
    return text_list


filename = "Transactions1.txt"
print(process_transactions(filename))
