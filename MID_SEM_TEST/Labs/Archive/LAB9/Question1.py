
user_input = input("Please enter some lowercase text: ")
user_input_split = user_input.split(". ")
capitalized_sentences = []

for sentence in user_input_split:
    capitalized_sentence = sentence[0].upper() + sentence[1:]
    capitalized_sentences.append(capitalized_sentence)

formatted = '. '.join(capitalized_sentences)


print(formatted)
