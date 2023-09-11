def get_polygonal_numbers(sides, terms):
    s = sides
    n = terms
    answer_list = []
    while n != 0:
        answer = ((s - 2) * (n**2) - (s - 4) * n) / 2
        answer_list.append(answer)
        n + 1
        return answer_list









print(f"First 5 triangular numbers are: {get_polygonal_numbers(3, 5)}")
# First 5 triangular numbers are: [1, 3, 6, 10, 15]

