def get_letter_frequency(text):
    text_list = []
    text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    #text = text.split()
    frequency = 0 
    for i in text:
        text_list.append(i)
    for i in text:
        if 




text = "The quick brown fox jumps over the lazy dog"
letter_freq_list = get_letter_frequency(text)
print(f"Letter Frequencies: {letter_freq_list}")