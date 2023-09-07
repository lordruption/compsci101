def get_polygonal_numbers(s, n):
    answer_list = []
    while n > 0:
        answer  = ((s-2) * n * n - (s - 4) * n) / 2
        answer_list.append(int(answer))
        n = n - 1    
    answer_list.reverse()
    return(answer_list)





print(f"First 5 triangular numbers are: {get_polygonal_numbers(3, 5)}")
