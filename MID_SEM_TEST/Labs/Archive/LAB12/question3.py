def calculate_cars_needed(number_of_people, number_of_seats):
    cars_needed_unrounded = number_of_people / number_of_seats
    if cars_needed_unrounded % 1 == 0:
        unrounded = int(cars_needed_unrounded)
        print(f"{unrounded} cars needed for {number_of_people} people.")
    elif cars_needed_unrounded // 1 != 0 or cars_needed_unrounded < 1:
        cars_needed_flat = cars_needed_unrounded // 1
        cars_needed = cars_needed_flat + 1
        intcars_needed = int(cars_needed)
        if intcars_needed == 1:
            print(f"{intcars_needed} car needed for {number_of_people} people.")
        else:
            print(f"{intcars_needed} cars needed for {number_of_people} people.")
# Test Case
calculate_cars_needed(10, 4) #3
calculate_cars_needed(4, 5) #1
calculate_cars_needed(21, 6) #4
calculate_cars_needed(42, 7) #6
calculate_cars_needed(4, 5) #1
