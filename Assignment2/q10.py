def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    input_stream.close()
    print(content)

def handle_high_scores(high_scores_dict, name, score, high_score_filename):
    create_file = open(high_score_filename, "w")
    high_scores_dict[name] = score


    

    










high_scores_dict = {'Ann': 35, 'Damir': 32, 'Andrew': 33, 'John': 19, 'Barry':29}
high_score_filename = 'echa347.txt'
handle_high_scores(high_scores_dict, "Robert", 17, high_score_filename)
print("\nFile contents:\n")
print_contents(high_score_filename)