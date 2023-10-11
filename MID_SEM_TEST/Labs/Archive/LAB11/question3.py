import math

def calculate_cars_needed(number_of_people, number_of_seats):
    cars_needed = 0
    if number_of_people % number_of_seats == 0:
        cars_needed = int(number_of_people / number_of_seats)
        if cars_needed == 1:
            return(print(f"{cars_needed} car needed for {number_of_people} people."))
        elif cars_needed > 1:
            return(print(f"{cars_needed} cars needed for {number_of_people} people."))
    elif number_of_people % number_of_seats != 0:
        cars_needed = math.ceil(number_of_people / number_of_seats)
        if cars_needed == 1:
            return(print(f"{cars_needed} car needed for {number_of_people} people."))
        elif cars_needed > 1:
            return(print(f"{cars_needed} cars needed for {number_of_people} people."))

calculate_cars_needed(4, 5)