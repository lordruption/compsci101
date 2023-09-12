line1 = input("Enter the first line of data: ").split(" ")
line2 = input("Enter the second line of data: ").split(" ")
merged_data = []
length = len(line1)

for i in range(length):
    if line1[i].isdigit() and line2[i].isdigit() or line1[i].startswith("-") or line2[i].startswith("-"):
        merged_data.append(int(line1[i]) + int(line2[i]))
    else:
        merged_data.append(line1[i] + line2[i])
print(f"The merged data is:", merged_data)




#1 2 3 4 5
#6 seven -8 25 31
#The merged data is: [7, 9, 11, 13, 15]
