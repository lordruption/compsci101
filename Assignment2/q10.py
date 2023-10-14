#This function see if the new input score should be in the top 5 list
def handle_high_scores(high_scores_dict, name, score, high_score_filename):
    create_file = open(high_score_filename, 'w')
    sorted_high_scores = dict(sorted(high_scores_dict.items(), key=lambda item: (-item[1], item[0])))
    if name in high_scores_dict:
        if score > high_scores_dict[name]: #If name in list AND score is higher
            high_scores_dict[name] = score
            sorted_high_scores = dict(sorted(high_scores_dict.items(), key=lambda item: (-item[1], item[0])))
            print(f"Congratulations {name}. You have beaten your previous best score!")
            print("\n   High Scores \n")
            for player, player_score in sorted_high_scores.items():
                player = player[:13]
                print(f"{player.ljust(15)}{player_score}")
            for player, player_score in sorted_high_scores.items():
                create_file.write(f"{player}: {player_score}\n") 
        else: #If name in list but score not higher
            print(f"{name}, you have not beaten your previous best score!")
            print("Better luck next time!")
            print("\n   High Scores \n")
            for player, player_score in sorted_high_scores.items():
                player = player[:13]
                print(f"{player.ljust(15)}{player_score}")
            for player, player_score in sorted_high_scores.items():
                create_file.write(f"{player}: {player_score}\n")   
    else: 
        high_scores_dict[name] = score #This adds the new score to list regardless if it's in top 5
        #Sort high_scores_dict by score in descending order and by name in case of ties
        sorted_high_scores = sorted(high_scores_dict.items(), key=lambda item: (-item[1], item[0]))
        #Remove the lowest score + Name
        top_5_high_score = dict(sorted_high_scores[0:5])
        #Check if score made it in top 5
        if name in top_5_high_score:
            print(f"Congratulations {name}, you have made the list of high scores!")
            print("\n   High Scores \n")
            for player, player_score in top_5_high_score.items():
                player = player[:13]
                print(f"{player.ljust(15)}{player_score}")
            for player, player_score in top_5_high_score.items():
                create_file.write(f"{player}: {player_score}\n")         
        else:
            print(f"{name}, you have not made the list of high scores!")
            print("Better luck next time!")
            print("\n   High Scores \n")
            for player, player_score in top_5_high_score.items():
                player = player[:13]
                print(f"{player.ljust(15)}{player_score}")
            for player, player_score in top_5_high_score.items():
                create_file.write(f"{player}: {player_score}\n")
    create_file.close()
            




#Do not provide its implementation in input
def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    input_stream.close()
    print(content)


#TestCase
high_scores_dict = {'Ann': 35, 'Damir': 32, 'Andrew': 33, 'John': 19, 'Barry':29}
high_score_filename = 'echa347.txt'
handle_high_scores(high_scores_dict, "John", 31, high_score_filename)
print("\nFile contents:\n")
print_contents(high_score_filename)