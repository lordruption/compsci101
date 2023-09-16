def shift_text(text):
    first_char = text[-1]
    remaining_char = text[::1] 
    answer = list(first_char + remaining_char)
    answer.pop(-1)
    answer_formatted = ''.join(answer)
    return answer_formatted







text = "Damir"
print("Text:", text, "Shifted Text:", shift_text(text))
# rDami
