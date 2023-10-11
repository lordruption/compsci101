#Calculate the acceleration
final_velocity = 100
initial_velocity = 50
time_passed = 20

step_1 = final_velocity - initial_velocity
step_2 = step_1 / time_passed
rounded_acceleration = round(step_2, 1)

acceleration = rounded_acceleration

print("The acceleration is", acceleration)