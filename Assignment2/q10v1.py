def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    input_stream.close()
    print(content)

def handle_high_scores(high_scores_dict, name, score, high_score_filename):
    # Update the high_scores_dict with the current player's score
    if name in high_scores_dict:
        if score > high_scores_dict[name]:
            print(f"Congratulations {name}. You have beaten your previous best score!")
            high_scores_dict[name] = score
        else:
            print(f"{name}, you have not beaten your previous best score!\nBetter luck next time!")
    else:
        high_scores_dict[name] = score
    
    # Sort high_scores_dict by score in descending order and by name in case of ties
    sorted_high_scores = sorted(high_scores_dict.items(), key=lambda item: (-item[1], item[0]))

    if name in sorted_high_scores:
        print(f"Congratulations {name}, you have made the list of high scores!")
    else:
        print(f"{name}, you have not made the list of high scores!\nBetter luck next time!")

    # Print the top 5 high scores
    print("\n   High Scores \n")
    for i, (player, player_score) in enumerate(sorted_high_scores[:5]):
        player = player[:13]  # Truncate names longer than 13 characters
        print(f"{player.ljust(15)}{player_score}")

    # Write the top 5 high scores to the specified text file
    with open(high_score_filename, 'w') as file:
        for player, player_score in sorted_high_scores[:5]:
            file.write(f"{player}: {player_score}\n")
    






#TestCase
high_scores_dict = {'Ann': 35, 'Damir': 32, 'Andrew': 33, 'John': 19, 'Barry':29}
high_score_filename = 'echa347.txt'
handle_high_scores(high_scores_dict, "Robert", 17, high_score_filename)
print("\nFile contents:\n")
print_contents(high_score_filename)