user_input = input("Enter sentences: ") # Takes UserInput
sentence = user_input[0].upper() + user_input[1:] # Capitalizes First letter of then entire string

sentence_length = len(sentence)

for i in range(1,sentence_length):
    if ((sentence[i] == "." or sentence[i] == "!" or sentence[i] == "?") and i != len(sentence) -1):
        sentence = sentence[:i+2] + sentence[i+2].upper() + sentence[i+3:]


print(sentence)




#chen is gay. chen is gay! chen is gay? ok