def display_menu():
    print("***********************")
    print("Simple Contacts Program")
    print("***********************")
    print("1. Display contact info")
    print("2. Add a new contact")
    print("3. Save and Exit")
def get_user_selection():
    answers = ['1', '2', '3']
    answer = input('Enter selection: ')
    while answer not in answers:
        print("Invalid input!")
        answer = input('Enter selection: ')
    else:
        return int(answer)

    






print(get_user_selection())