perfect_square = []
# Import math Library
import math

prompt_start = "Enter the start: "
prompt_end = "Enter the end: "

start = int(input(prompt_start))
end = int(input(prompt_end))

for number in range(start,end):
    if math.sqrt(number) % 1 == 0:
        perfect_square.append(number)

result = ' '.join(map(str, perfect_square))

print(result)



    
