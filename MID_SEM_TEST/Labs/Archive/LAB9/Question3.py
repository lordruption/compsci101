empty_list = []

start_prompt = "Enter the start: "
end_prompt = "Enter the end: "
start = int(input(start_prompt))
end = int(input(start_prompt))

if start % 2 == 1:  # Check if 'start' is an odd number
    start += 1  # Increment 'start' by 1

for number in range(start, end, 2):
    empty_list.append(number)

result = ' '.join(map(str, empty_list))
print(result)