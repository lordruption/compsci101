speed = 60
reaction_time = 1.5
friction_coefficient = 0.7 
perception_coefficient = 0.278
distance_factor = 254

step_1 = perception_coefficient * speed * reaction_time
speed_squared = speed * speed
step_2 = distance_factor * friction_coefficient
step_3 = speed_squared / step_2
answer_1 = step_1 + step_3
answer = round(answer_1, 2)

print("The stopping distance is", answer, "metres.")