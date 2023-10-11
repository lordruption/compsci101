# Set up initial list of names
names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]
# Display the names to the user
print("Current list of names:", names)
# Ask user for action
action = input("Enter A to add a name or D to delete a name: ")
if action == "A": # Add a new name
    new_name = input("Enter a new name: ")
    
    # Keep asking user for an existing name until they enter a valid name
    before_name = input("Enter the name you want to insert the new name before: ")
    while before_name not in names:
        print(before_name, "is not in the list of names!")
        before_name = input("Enter the name you want to insert the new name before: ")
        
    # Add the new name in the correct location
    before_name_index = names.index(before_name)
    names.insert(before_name_index, new_name)
else:
    # Repeatedly ask user to enter a name to delete until the enter a valid name
    name_to_delete = input("Enter a name to delete: ")
    while name_to_delete not in names:
        print(name_to_delete, "is not in the list of names!")
        name_to_delete = input("Enter a name to delete: ")
    
    # Remove the specified name from the list
    name_to_delete_index = names.index(name_to_delete)
    names.pop(name_to_delete_index)
 
# Print the updated list of names
print("Updated list of names:", names)