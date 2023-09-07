#empty list
shopping_list = []
number = 0
#user prompt
item = input("Please enter an item for your shopping list or end to print the list: ")
#for loop
while item != "end":
    shopping_list.append(item)
    item = input("Please enter an item for your shopping list or end to print the list: ")

shopping_list.sort()
print()
print("Shopping List:")
print("==============")

item_number = shopping_list

for item in shopping_list:
    number = number + 1
    print(f"{number}) {item}")