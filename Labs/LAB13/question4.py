import math
def main():
    while True:
        display_menu()
        user_option = get_user_option_input("Enter selection: ")
        if user_option == '1':
            wallpaper_roll_width = float(input("Enter the wallpaper roll width: "))
            wallpaper_roll_length = float(input("Enter the wallpaper roll length: "))
            room_length = float(input("Enter the length of the room: "))
            room_width = float(input("Enter the width of the room: "))
            room_height = float(input("Enter the height of the room: "))
            calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length)
        elif user_option == '0':
            print("See you next time!")
            break
def display_menu():	
    print("************************")
    print("1. Wallpaper Calculation")
    print("0. Exit")
    print("************************")
def get_user_option_input(prompt_message):
    while True:
        answer = input(prompt_message)
        if answer == '1':
            wallpaper_roll_width = float(input("Enter the wallpaper roll width: "))
            wallpaper_roll_length = float(input("Enter the wallpaper roll length: "))
            room_length = float(input("Enter the length of the room: "))
            room_width = float(input("Enter the width of the room: "))
            room_height = float(input("Enter the height of the room: "))
            calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length)
        elif answer == '0':
            print("See you next time!")
            break
        else:
            continue
def calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length):
    # Calculate the number of whole strips per roll
    strips_per_roll = math.floor(wallpaper_roll_length / room_height)
    # Calculate the room perimeter
    room_perimeter = 2 * (room_width + room_length)
    # Calculate the total number of whole strips needed to cover the full room
    total_strips_needed = math.ceil(room_perimeter / wallpaper_roll_width)
    # Calculate the total number of rolls needed
    total_rolls_needed = math.ceil(total_strips_needed / strips_per_roll)
    print(f"The total number of wallpaper rolls needed for this room is {total_rolls_needed}")
main()
