def process_transactions(filename):
    processed_transactions = []  # Step 1
    balances = []  # Step 2
    for transaction in filename:  # Step 3
        # Split the transaction into name and amount
        name, amount_str = transaction.split(':')  # Step 4
        # Check if the person's name is already in balances
        found = False
        for i in range(len(balances)):
            person, balance = balances[i]

            if person == name:
                # Update the balance based on the transaction amount
                balance = int(balance) + int(amount_str)
                balances[i] = (person, balance)  # Update the balance
                found = True
                break

        if not found:
            # If the person is not in balances, add them with the initial balance
            balances.append((name, int(amount_str)))

        # Now, you can format and append the transaction to processed_transactions (Step 6)
        processed_transactions.append(f'{name}:{balance}')
    return processed_transactions


filename = ['Jennine:0', 'Abdelmoula:500', 'Ornella:-200', 'Jennine:-300', 'Abdelmoula:-150', 'Costinel:250', 'Jennine:427', 'Costinel:-90', 'Abdelmoula:-120', 'Costinel:107', 'Jennine:23', 'Ornella:139', 'Asad:67', 'Asad:23', 'Asad:100', 'Jennine:217']
transaction_data = process_transactions(filename)
print(transaction_data)


# In this version I will hard code the data in the program
