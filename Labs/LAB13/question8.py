def carry_out_transactions(balance, transactions_tuple):
    deposits = 0
    withdrawals = 0
    for i in transactions_tuple:
        if i >= 0:
            deposits = deposits + i
        elif i < 0:
            withdrawals = withdrawals + i
    balance = balance + deposits + withdrawals
    withdrawals_removed_variable = withdrawals * -1
    result = (balance, deposits, withdrawals_removed_variable)
    return result








results = carry_out_transactions(5400, (100, -400, 500, -800, 600, -100, -200, 50, 0, -200))
print("Balance $", results[0], ", deposits $", results[1], ", withdrawals $", results[2], sep="")