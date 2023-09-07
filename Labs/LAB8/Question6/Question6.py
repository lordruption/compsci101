# Initialize variables to keep track of assignment statistics
Assignment_sum_result = 0  # Total score of submitted assignments
number_of_assignment = 0   # Total number of submitted assignments
missed_assignments = 0      # Total number of missed assignments

# Input assignment data from the user
assignment_data_list = input("Enter assignment data: ").split(",")

# Calculate the total score and count missed assignments
for number in assignment_data_list:
    if number == "":
        missed_assignments += 1
    else:
        Assignment_sum_result += float(number)

# Calculate the number of submitted assignments
number_of_assignment = len(assignment_data_list) - missed_assignments

# Calculate and display the average score
if Assignment_sum_result != 0 and number_of_assignment != 0:
    average = Assignment_sum_result / number_of_assignment
    rounded_average = round(average, 2)
    # Display the calculated statistics
    print("Number of missed assignments:", missed_assignments)
    print("Average assignment score:", rounded_average)
else: 
    print("Number of missed assignments:", missed_assignments)
    print("Average assignment score: Undefined")
