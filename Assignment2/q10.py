def handle_high_scores(high_scores_dict, name, score, high_score_filename):
















#TestCase
high_scores_dict = {'Ann': 35, 'Damir': 32, 'Andrew': 33, 'John': 19, 'Barry':29}
high_score_filename = 'echa347.txt'
handle_high_scores(high_scores_dict, "Robert", 17, high_score_filename)
print("\nFile contents:\n")
print_contents(high_score_filename)