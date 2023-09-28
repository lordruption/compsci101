def get_inventory(filename):
    inventory = {}  # Initialize an empty dictionary to store the inventory.
    try:
        with open(filename, 'r') as file:
            # Skip the first line (heading).
            next(file)
            for line in file:
                # Split the line into item and price using tab ("\t") as the delimiter.
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    item, price = parts
                    inventory[item] = float(price)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return inventory

# Example usage:
filename = "Inventory1.txt"
inventory = get_inventory(filename)
for item in sorted(inventory):
    print(f"{item} => ${inventory[item]}")