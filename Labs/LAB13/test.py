def get_letter_frequency(text):
    # Initialize a dictionary to store letter frequencies
    letter_freq = {}

    # Iterate through each character in the text
    for char in text:
        # Check if the character is an alphabetical letter
        if char.isalpha():
            # Convert the character to lowercase to ignore case
            char = char.lower()

            # Update the frequency count in the dictionary
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1

    # Convert the dictionary to a list of tuples and sort it alphabetically
    letter_freq_list = sorted(letter_freq.items())

    return letter_freq_list

# Example usage:
text = "The quick brown fox jumps over the lazy dog"
letter_freq_list = get_letter_frequency(text)
print(f"Letter Frequencies: {letter_freq_list}")
