def get_high_scores(filename):
    dict_name_score = {}
    with open(filename, 'r', encoding='utf-8') as input_stream:
        for line in input_stream:
            line = line.strip()  # Remove leading/trailing white spaces
            if not line:
                continue  # Skip empty lines
            parts = line.split(':')
            if len(parts) == 2:
                name, score = parts
                dict_name_score[name] = int(score)
            else:
                print(f"Skipped line: {line} (malformed data)")
    return dict_name_score



print(get_high_scores("HighScores.txt"))
