import math

side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))


side_c_squared = (side_a * side_a) + (side_b * side_b)

side_c = round(math.sqrt(side_c_squared), 2)



print("The length of the hypotenuse is", side_c)
