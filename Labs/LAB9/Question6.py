# Prompt the user to input a line of integers separated by commas
line_of_integers = input("Enter a line of integers: ").split(",")

# Initialize variables to store the minimum and maximum numbers
minimum_number = int(line_of_integers[0])
maximum_number = int(line_of_integers[0])


# Loop through each integer in the input list to find the minimum number
for i in line_of_integers:
    if int(i) <= int(minimum_number):
        minimum_number = i

# Loop through each integer in the input list to find the maximum number
for i in line_of_integers:
    if int(i) >= int(maximum_number):
        maximum_number = i

# Display the minimum and maximum numbers found
print(f"The minimum number is {minimum_number} and the maximum number is {maximum_number}.")

#600,500,400,300,200,0,-100