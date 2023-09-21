value_of_x = 0.2

question2 = 1 / (1 - value_of_x)
question3 = (1 + value_of_x) + (value_of_x * value_of_x) + (value_of_x * value_of_x * value_of_x)
question4 = round(question2 - question3, 3)


print("The value of x is", value_of_x)
print("The result of the operation 1/(1-x) is", question2)
print("The result of the Taylor's Series is", question3)
print("The difference between the results is", question4)