# Prompting the user to input a line of integers separated by commas
line_of_integers = input("Enter a line of integers: ")

# Splitting the input line into a list of individual integer strings using commas as the delimiter
list_of_integers = line_of_integers.split(",")

# Converting the individual integer strings into actual integer values
for i in range(len(list_of_integers)):
    list_of_integers[i] = int(list_of_integers[i])

# Finding the maximum and minimum values from the list of integers
max_num = max(list_of_integers)
min_num = min(list_of_integers)

# Displaying the minimum and maximum values to the user
print(f"The minimum number is {min_num} and the maximum number is {max_num}.")
