#input
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

#while-loop
while start >= end:
    print(start, end=" ")
    start = start - 1