empty_list = []
# Prompt the user to enter the start and end values
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
start_proper = start + 1


for number in reversed(range(end, start_proper)):
    empty_list.append(number)



result = ' '.join(map(str, empty_list))
print(result)