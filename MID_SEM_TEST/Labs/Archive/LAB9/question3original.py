start_prompt = "Enter the start: "
end_prompt = "Enter the end: "
start = int(input(start_prompt))
end = int(input(start_prompt))
counter = start
while counter < end:
    if counter % 2 == 0:
        print(counter, end=" ")
    counter += 1
print()