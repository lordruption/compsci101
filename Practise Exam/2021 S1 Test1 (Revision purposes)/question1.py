def get_funny_average(number_string, sentinel_value):
    answer = 0 
    while answer < sentinel_value:
        for i in answer:
            if i < 0:
                pass
            elif i > sentinel_value:
                pass
            else:
                answer + i
                return answer

for char in number_string:
    if char == ",":
        append()






number_string = "21.543,35.814"
sentinel_value = 32.9908
print("The funny average is:", get_funny_average(number_string, sentinel_value))