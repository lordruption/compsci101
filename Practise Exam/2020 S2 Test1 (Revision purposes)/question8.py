prompt_amount = int(input("Enter a donation amount (up to 1000): "))
#prompt_instalments = "Enter the number of payment instalments: "

while prompt_amount > 1000 or prompt_amount < 1:
    prompt_amount = int(input("Enter a donation amount (up to 1000): "))
else:
    prompt_instalments = int(input("Enter the number of payment instalments: "))

monthly_amount = prompt_amount // prompt_instalments
instalments = int(prompt_amount / monthly_amount)


print(f"You will donate {prompt_amount} dollars in {instalments} instalments of {monthly_amount} dollars.")

'''
if instalments // 1 != 0:
    round_installment = round(instalments)
    print(round_installment)
else:
    print(instalments)
'''

'''
-1
1001
100
5
'''