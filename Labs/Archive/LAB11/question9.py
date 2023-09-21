def word_puzzle(horizontal_str, vertical_str):
  # Initialize the blank number.
  blank_num = 0

  # Iterate over each character in the horizontal string.
  for c in horizontal_str:
    # Find the index of c in the vertical string.
    index = vertical_str.find(c)

    # If c is found in the vertical string, break the loop.
    if index != -1:
      break
    else:
      # Increment the blank number.
      blank_num += 1

  # If c is not found in the vertical string, print the message.
  if index == -1:
    print("The two strings do not intersect")
    return

  # Print the two strings, with blank spaces added to the left of the horizontal string
  # for the number of characters that are not shared.
  for i in range(len(vertical_str)):
    if i == index:
      print(horizontal_str)
    else:
      print(' ' * blank_num + vertical_str[i])

word_puzzle("hello","world")
