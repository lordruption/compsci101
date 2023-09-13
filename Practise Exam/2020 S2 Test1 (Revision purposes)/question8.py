prompt_amount = "Enter a donation amount (up to 1000): "
prompt_instalments = "Enter the number of payment instalments: "



while 1000 < prompt_amount or prompt_amount < 0:
    prompt_amount = input("Enter a donation amount (up to 1000): ")
    if 0 <= prompt_amount <= 1000:
        break
    else:
        prompt_amount = int(input("Enter a donation amount (up to 1000): "))
