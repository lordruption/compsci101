# Initialize a list for unique words
empty_list = []
list_removed_duplicates = []
# User Input - sentence
sentence = input("Please enter a sentence: ")
# Split the sentence into words
sentence = sentence.split()

for word in sentence:
    empty_list.append(word)

for word in empty_list:
    if word not in list_removed_duplicates:
        list_removed_duplicates.append(word)
list_removed_duplicates.reverse()

# Join the unique words into a formatted string
unique_words_formatted = ", ".join(list_removed_duplicates)
# Print the reversed list
print("Unique words:", unique_words_formatted)