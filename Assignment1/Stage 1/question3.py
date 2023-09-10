def get_width(board):
    board_list = []
    board_list.append(board)
    width = len(board[0])
    return (width)


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


def display_board(board):
  height = len(board)
  width = len(board[0])
  
  for i in range(height-1, -1, -1):
    print('|' + ' '.join(board[i]) + '|')
  
  print('|' + '-' * (2 * width - 1) + '|')
  
  print('|' + ' '.join(str(i) for i in range(width)) + '|')

board = create_board(9, 7)
display_board(board)