import math
def calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length):
    # Calculate the number of whole strips per roll
    strips_per_roll = math.floor(wallpaper_roll_length / room_height)

    # Calculate the room perimeter
    room_perimeter = 2 * (room_width + room_length)

    # Calculate the total number of whole strips needed to cover the full room
    total_strips_needed = math.ceil(room_perimeter / wallpaper_roll_width)

    # Calculate the total number of rolls needed
    total_rolls_needed = math.ceil(total_strips_needed / strips_per_roll)

    return int(total_rolls_needed)



print(calculate(2, 4, 2.1, 0.53, 10.05))


'''	
Enter the wallpaper roll width: 0.53
Enter the wallpaper roll length: 10.05
Enter the length of the room: 4
Enter the width of the room: 2
Enter the height of the room: 2.1
The total number of wallpaper rolls needed for this room is 6
'''