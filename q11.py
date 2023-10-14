import random

def main(): #Do not alter in any way!
    filename = "TeReoMaori_to_English_Dictionary.txt"
    high_score_filename = "HighScores.txt"
    output_filename = 'echa347.txt'
    file_contents = read_dictionary_file(filename)
    maori_english_dict = get_maori_english_dictionary(file_contents)
    high_scores_dict = get_high_scores(high_score_filename)
    name = input("Please enter your name: ")
    play_game(maori_english_dict, high_scores_dict, name, output_filename)
    
def get_five_dictionary_items(maori_english_dict): #Do not alter in any way!
    dictionary_items = []
    maori_words = list(maori_english_dict.keys())
    while len(dictionary_items) < 5:
        random_index = random.randrange(0, len(maori_words))
        dictionary_item = maori_words[random_index], maori_english_dict[maori_words[random_index]]
        while dictionary_item in dictionary_items:
            random_index = random.randrange(0, len(maori_words))
            dictionary_item = maori_words[random_index], maori_english_dict[maori_words[random_index]]
        dictionary_items.append(dictionary_item)
    return dictionary_items

def get_question_index(question_items): #Do not alter in any way!
    return random.randrange(len(question_items))

#This function reads filename.txt - Q1
def read_dictionary_file(filename):
    input_stream = open(filename, 'r', encoding='utf-8')
    #This function split file by new line
    read_file = input_stream.read().split('\n')
    input_stream.close()
    return read_file

#This function takes a string list then returns it in dictionary format - Q2
def get_maori_english_dictionary(contents):
    maori_english_dictionary = {}
    listcontent = list(contents)
    for item in listcontent:
        #This turns 'Waipuke - Flood' to 'Waipuke': 'Flood'
        split_item = item.split(" - ")
        key = split_item[0]
        value = split_item[-1]
        maori_english_dictionary[key] = value
    return maori_english_dictionary

#This function prints user's name and game instruction - Q4
def print_quiz_info(name):
    name_length = len(name)
    #This prints specific amount of * so that its the lenght of name
    print("*" * 33 + "*" * name_length)
    print(f"*Welcome {name} to the Reo Māori Quiz!*")
    print("*" * 33 + "*" * name_length)
    #Below is standard output DO NOT CHANGE
    print()
    print("The quiz has 5 rounds.")
    print("In each round you have to work out the English meaning of a Māori word.")
    print("You are given 5 options to select from and 3 attempts to select the right one.")
    print("Get the right answer and you score 1 point for the round.")
    print("Otherwise you score 0 points for the round.")
    print("Good luck!")

#This function takes user_selection but it to be in the range of 1 to 5 - Q5
def get_user_selection():
    while True:
        selection = input("Enter your selection (1 to 5): ")
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= 5:
                return selection
        print("Please enter a number from 1 to 5")

#This function plays a single round of the Reo Māori Quiz - Q6
def play_round(question_items, question_index):
    attempts = 3
    target_word = question_items[question_index][0]
    target_key_int = int(question_index + 1)
    target_meaning = question_items[question_index][1]
    print(f"Select the definition for the word {target_word}")
    print()
    print("Choose from one of the following options:")
    print()
    iteration = 1
    for answer in question_items:
        print(f"{iteration}) {answer[1]}")
        iteration = iteration + 1
    print()
    while attempts > 0:
        user_selection = get_user_selection()
        attempts = attempts - 1
        if user_selection == target_key_int:
            print()
            print(f"Congratulations! {target_word} does mean '{target_meaning}'!")
            return 1
        else:
            print("Your answer is incorrect.")
            if attempts > 0:
                print(f"You have {attempts} attempt(s) left. Please try again.")
            print()
            continue
    else:
        print(f"You have not identified the meaning of {target_word}")
        print(f"{target_word} means '{target_meaning}'")
        print("Better luck next time!")
        return 0
    

#This function see if the new input score should be in the top 5 list - Q10
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

#This function plays one game with 5 rounds
def play_game(maori_english_dict, high_scores_dict, name, output_filename):
    print_quiz_info(name)
    round_count = 0
    final_quiz_score = 0
    while round_count < 5:
        question_items = get_five_dictionary_items(maori_english_dict)
        round_count += 1
        question_index = get_question_index(question_items)
        print()
        print("Round", round_count)
        print()
        score = play_round(question_items, question_index)
        if score == 1:
            final_quiz_score += 1
            continue
        elif score == 0:
            continue
    else:
        print()
        print("Your final quiz score is:", final_quiz_score)
        quit






#TestCase
random.seed(10)    
main()
print("\nFile Contents\n")
print_contents('echa347.txt')