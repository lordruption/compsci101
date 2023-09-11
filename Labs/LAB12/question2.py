import math

def calculate_frustum_volume(height, radius1, radius2):
    pixheightdividethree = (math. pi * height) / 3
    rtwooverrone = radius2 / radius1
    multiply = radius1 * radius2
    twoovertwo = radius2 / 2
    volume = pixheightdividethree(rtwooverrone + multiply + twoovertwo)
    return volume








height = 10
radius1 = 8
radius2 = 4
volume = calculate_frustum_volume(height, radius1, radius2)
print("The volume is", volume)