import math
people = int(input("Enter the number of people: "))
drink_ml= 200
barrel_ml = 200 * 65

ml_needed = people * drink_ml
barrrel_made = math.ceil(ml_needed / barrel_ml)
ml_made = barrrel_made * barrel_ml
ml_wasted = ml_made - ml_needed
drink_wasted = int(ml_wasted / 200)


print(f"{drink_wasted} drinks ({ml_wasted}ml) are wasted.")