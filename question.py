def get_inventory(filename):
    inventory = {}
    open_file = open(filename, 'r')
    file = open_file.readlines()
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 2:
            item_name = parts[0]
            item_price = str(parts[-1])
            inventory[item_name] = item_price
    open_file.close()
    del inventory['Item']  
    return inventory
    
filename = "Inventory1.txt"
inventory = get_inventory(filename)
print(inventory)