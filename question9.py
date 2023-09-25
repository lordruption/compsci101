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
def print_contact_info(contact_info):
    if contact_info == None:
        print("Contact not found")
    else:
        name = contact_info[0]
        phone = contact_info[1]
        email = contact_info[2]
        print(f"Name: {name} Phone: {phone} Email: {email}")
def add_contact(contact_list):
    print("Please enter the new contact's details")
    name = input("Contact's Name: ")
    phone_number = input("Contact's Phone Number: ")
    email = input("Contact's Email address: ")
    print("Contact added")
    new_contact = (name, phone_number, email)
    contact_list.append(new_contact)
def save_contacts(contact_list, filename):
    open_file = open(filename, 'w')
    flat_contact_list = [item for contact in contact_list for item in contact]
    for item in flat_contact_list:
        open_file.write(item + '\n')   
    open_file.close()
def main():
    display_menu()
    get_user_selection()





main()
print()
print_contents('echa347.txt')
