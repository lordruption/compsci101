# Initialize a list of names
names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]

# Display the current list of names to the user
print("Current list of names:", names)

# Prompt the user for their desired action (add or delete)
action = input("Enter A to add a name or D to delete a name: ")

if action == "A":
    # Gather the new name to be added
    new_name = input("Enter a new name: ")

    # Ensure the selected insertion point is valid
    before_name = input("Enter the name you want to insert the new name before: ")
    while before_name not in names: 
        print(f"{before_name} is not in the list of names!")
        before_name = input("Enter the name you want to insert the new name before: ")

    # Insert the new name at the correct position
    before_name = names.index(before_name)
    names.insert(before_name, new_name)
else:
    # Repeatedly request a name for deletion until a valid name is provided
    name_to_delete = input("Enter a name to delete: ")
    while name_to_delete not in names:
        print(f"{name_to_delete} is not in the list of names!")
        name_to_delete = input("Enter a name to delete: ")

    # Remove the specified name from the list
    name_to_delete_index = names.index(name_to_delete)
    names.pop(name_to_delete_index)

# Display the updated list of names
print("Updated list of names:", names)
