def convert_to_percent(scores_list, out_of):
    marks = []
    for i in scores_list:
        answer = (i / out_of) * 100
        marks.append(round(answer))  # Round the result to the nearest integer

# DO not change code under here
marks = [25.5, 50, 49, 15.9, 0]
convert_to_percent(marks, 50)
print("Marks out of 100:", marks)
