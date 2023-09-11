import math


def to_the_power_of():
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    result = int(math.pow(num_1,num_2))
    answer = (f"{num_1} to the power of {num_2} is {result}")
    return(answer)






print(to_the_power_of())
