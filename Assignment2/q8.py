def get_high_scores(filename):
    dict_name_score = {}
    input_stream = open(filename, 'r', encoding='utf-8')
    read_file = input_stream.read().split('\n')
    input_stream.close()
    for item in read_file:
        name, score = item.split(':')
        dict_name_score[name] = int(score)
    return dict_name_score


print(get_high_scores("HighScores1.txt"))
