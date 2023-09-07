import math

people = int(input("Enter the number of people: "))
slices = int(input("Enter the number of slices in each cake: "))


num_cake = people / slices

num_cake_up = math.ceil(num_cake)



print(num_cake_up, "cakes are needed.")
