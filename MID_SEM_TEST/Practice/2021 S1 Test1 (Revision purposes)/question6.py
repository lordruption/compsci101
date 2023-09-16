def get_triangle_type(side_length1, side_length2, side_length3):
    if side_length1 == side_length2 and side_length2 == side_length3:
        return f"Sides are {side_length1}, {side_length2} and {side_length3}. It is a equilateral triangle."
    elif side_length1 == side_length2 or side_length2 == side_length3:
        return f"Sides are {side_length1}, {side_length2} and {side_length3}. It is an isosceles triangle."
    else: 
        return "Sides are 2, 3 and 4. It is a scalene triangle."
    





print(get_triangle_type(6, 6, 6))
