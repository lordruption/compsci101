def convert_to_percent(scores_list, out_of):
    for i in range(len(scores_list)):
        percentage = (scores_list[i] / out_of) * 100
        percentage_round = round(percentage, 2)
        marks[i] = percentage_round
        
















marks = [25.5, 50, 49, 15.9, 0]
convert_to_percent(marks, 50)
print("Marks out of 100:", marks)


#Marks out of 100: [51, 100, 98, 32, 0]
