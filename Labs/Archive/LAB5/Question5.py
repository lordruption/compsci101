base =  int(input("Enter the base: "))
height = int(input("Enter the height: "))
area = (base * height) / 2
#outputs
print(f"A triangle with base {base} and height {height} has an area of {area}")
another_triangle = str(input("Calculate another area (y/n)? "))

while another_triangle == "y":
    base =  int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = (base * height) / 2
    print(f"A triangle with base {base} and height {height} has an area of {area}")
    another_triangle = str(input("Calculate another area (y/n)? "))



