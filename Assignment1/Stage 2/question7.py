def play_turn(board, player):
  """
  Plays a turn for the given player on the given board.

  Args:
    board: The board to play on.
    player: The player to play for.

  Returns:
    The column where the player placed their piece.
  """
  prompt = "Player {} -- enter the column: ".format(player)
  while True:
    column = input(prompt)
    if column == 'quit':
      return None
    if column.isdigit() and 0 <= int(column) < len(board[0]):
      return int(column)



def create_board(width, height):
    width_list = []
    if height < 4:
        height = 4
    if width < 4:
        width = 4
    if height > 10:
        height = 10
    if width > 10:
        width = 10
    width_formatted = width * "."
    width_list.append(width_formatted)
    final_list = width_list * height
    return(final_list)






board = create_board(7, 6)
play_turn(board, "X")

#Chen is gay