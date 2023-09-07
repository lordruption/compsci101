

length = int(input("Enter the length of the room in metres: "))
width = int(input("Enter the width of the room in metres: "))
height = 2.4

ceilling = width * length * 30
walls = length * height * 2 * 25
walls2 = height * width * 2 * 25





total = round(ceilling + walls + walls2)
print("The total cost is $", total)