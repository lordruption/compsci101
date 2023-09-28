def word_analysis(text):










text = "The quick brown fox jumps over the lazy dog"
word_analysis_dict = word_analysis(text)
for key in sorted(word_analysis_dict):
    print(key, word_analysis_dict[key])