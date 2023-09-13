list1 = input("Enter the first line of data: ").split(" ")
list2 = input("Enter the second line of data: ").split(" ")
merged_data = []
length = len(list1)

for i in range(length):
    if ((list1[i].isdigit() or list1[i].startswith("-") and list1[i][1:].isdigit())
        and (list2[i].isdigit() or list2[i].startswith("-") and list2[i][1:].isdigit())):
        merged_data.append(int(list1[i]) + int(list2[i]))
    else:
        merged_data.append(list1[i] + list2[i])
print(f"The merged data is:", merged_data)




#1 2 3 4 -5
#6 seven -8 25 31
#The merged data is: [7, 9, 11, 13, 15]
