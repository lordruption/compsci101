# Define a function named 'update_dictionary' that takes two arguments:
# 'a_dict', which is a dictionary, and 'target_value', which is the value we want to find and remove from the dictionary.
def update_dictionary(a_dict, target_value):
    # Create an empty list named 'keys_to_delete' to store the keys that match the 'target_value'.
    keys_to_delete = []

    # Iterate through the items (key-value pairs) in the 'a_dict' dictionary.
    for key, value in a_dict.items():
        # Check if the 'value' associated with the current 'key' is equal to the 'target_value'.
        if value == target_value:
            # If it is, add the 'key' to the 'keys_to_delete' list.
            keys_to_delete.append(key)
    
    # Now that we have identified the keys to delete, iterate through the 'keys_to_delete' list.
    for key in keys_to_delete:
        # Delete the key-value pair associated with the 'key' from the 'a_dict' dictionary.
        del a_dict[key]

    # Finally, return the modified 'a_dict' after removing the key-value pairs with 'target_value'.
    return a_dict







a_dict = {"a":0, "b":0, "c":1, "d":1, "e":5} #This is the dictionary 
print("Before:", end=" ") #This prints the original dictionary
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()
update_dictionary(a_dict, 0) #This is where it calls my function
print("After:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()


#Below is the desired output
#Before: a:0 b:0 c:1 d:1 e:5 
#After: c:1 d:1 e:5 
