def write_words_start_vowel(filename, names):
    create_file = open(filename, "w")
    for item in names:
        first_letter = item[0].lower()
        if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
            create_file.write(item + '\n')
    create_file.close()







write_words_start_vowel('echa347.txt', ['life', 'is', 'a', 'long', 'journey', 'with', 'problems', 'to', 'solve'])