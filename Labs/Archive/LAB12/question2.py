import math

def calculate_frustum_volume(height, radius1, radius2):
    left = (math.pi * height) / 3
    right = radius1 ** 2 + radius1 * radius2 + radius2 ** 2
    answer = round(left * right, 2)
    return answer






print("The volume is", calculate_frustum_volume(7, 10, 9))
