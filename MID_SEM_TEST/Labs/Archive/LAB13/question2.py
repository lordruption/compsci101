def get_user_option_input(prompt_message):
    while True:
        answer = input(prompt_message)
        if answer == '1' or answer == '0':
            return int(answer)
        else:
            continue







print(get_user_option_input("Enter selection: ") )


