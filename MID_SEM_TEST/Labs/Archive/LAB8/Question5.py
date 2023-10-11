user_temperature_values_list = []      # Stores user-provided temperature values
extreme_temperatures_list = []          # Collects temperatures within the extreme range

user_temperature_values = str(input("Enter a line of temperature values: "))  # Prompt for user input

user_temperature_values_list = user_temperature_values.split(",")  # Splitting input into a list

# Removing any lingering commas from the list (if any)
if "," in user_temperature_values_list:
    user_temperature_values_list.remove(",")

# Converting the list of string values to a list of integers
integer_numbers = [int(num) for num in user_temperature_values_list]

# Identifying temperatures within the extreme range and storing them in the 'extreme_temperatures_list'
for num in integer_numbers:
    if num <= -10:
        extreme_temperatures_list.append(num)
    elif num >= 40:
        extreme_temperatures_list.append(num)

extreme_temperatures_list.sort()

list_as_string = ', '.join(map(str, extreme_temperatures_list))  # Converting the list to a comma-separated string

print("The extreme temperatures are:", list_as_string)  # Displaying the extreme temperatures
