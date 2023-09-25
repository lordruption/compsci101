def display_menu():# This Function display the menu selection
    print("***********************")
    print("Simple Contacts Program")
    print("***********************")
    print("1. Display contact info")
    print("2. Add a new contact")
    print("3. Save and Exit")
def get_user_selection():# This Function check if input is valid
    answers = ['1', '2', '3']
    answer = input('Enter selection: ')
    while answer not in answers:
        print("Invalid input!")
        answer = input('Enter selection: ')
    else:
        return int(answer)
def get_contacts(filename):
    return_list = []
    open_file = open(filename, 'r')
    read_file = open_file.read()
    split_file = read_file.split('\n')
    current_range_start = 0
    while current_range_start < len(split_file) - 2:
        contact_name = split_file[current_range_start]
        telephone_number = split_file[current_range_start + 1]
        email_address = split_file[current_range_start + 2]
        contact_tuple = (contact_name, telephone_number, email_address)
        return_list.append(contact_tuple)
        current_range_start += 3
    open_file.close()
    return return_list
def get_contact_info(contact_list, contact_name):
    for contact in contact_list:
        if contact[0] == contact_name:
            return contact
        else:
            continue




contact_list = [('Damir Azhar', '021-1234567', 'damir@emailprovider.com'),
                ('Ann Cameron', '022-7654321', 'ann@bmail.com')]
contact_info = get_contact_info(contact_list, "Ann Cameron")
print(contact_info)
