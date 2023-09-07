import math

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

answer = round((math.pi * radius * radius * height) / 3, 3)


print("Volume of the cone is", answer, "cubic cm.")