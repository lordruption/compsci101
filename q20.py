def get_student_averages(filename):
    students_data = {}
    open_file = open(filename, 'r')
    file = open_file.read()
    split_file = file.split('\n')
    for line in split_file:
        name, score = line.split(":")
        if name not in students_data:
            students_data[name] = [int(score)]
        elif name, score == None:
            continue
        else:
            students_data[name] += [int(score)]

    for name,score in students_data.items():
        total = sum(score)
        count = len(score)
        average = total / count
        students_data[name] = average
    open_file.close()
    return students_data






#TestCase
filename = "student_data1.txt"
student_data_dict = get_student_averages(filename)
print(f"Checking return type: {type(student_data_dict)}")
for student in sorted(student_data_dict.keys()):
    print(f"{student}'s average mark is {student_data_dict[student]}")
