def read_numbers(filename):
    text = open(filename, "r")
    textv1 = text.read().split()
    total = 0
    count = 0
    for i in textv1:
        total = total + int(i)
        count = count + 1
    average = total / count
    averagev1 = round(average, 1)
    return (total, averagev1)
    textv1.close()




filename = "Lab14Q03_2.txt"
print(read_numbers(filename))