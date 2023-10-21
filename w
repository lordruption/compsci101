def find_string(sentence, string_to_find):
    return sentence.lower().count(string_to_find.lower())

print(find_string("Funny people like to have Fun", "Fun"))


