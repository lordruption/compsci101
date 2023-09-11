'''
def convert_to_percent(scores_list, out_of):
    marks = []
    for i in scores_list:
        answer = (i / out_of) * 100
        marks.append(round(answer)) 
    return marks
'''

def convert_to_percent(scores_list, out_of):
    for i in range(len(scores_list)):
        percent = (scores_list[i] / out_of) * 100
        scores_list[i] = round(percent)




marks = [25.5, 50, 49, 15.9, 0]
convert_to_percent(marks, 50)
print("Marks out of 100:", marks)