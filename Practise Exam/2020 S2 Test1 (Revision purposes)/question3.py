def print_solution(operator, number1, number2):
    answer = ""
    if operator == "-":
        answer = number1 - number2
    elif operator == "+":
        answer = number1 + number2
    elif operator == "/":
        answer = number1 / number2
    elif operator == "*":
        answer = number1 * number2
    correct_answer = float(answer)
    print(correct_answer)
print_solution('*', 6, 2)
