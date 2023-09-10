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
def get_width(board):
    width = len(board[0])
    return (width)
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
def stage_1(width, height):
    board = create_board(width, height)
    display_board(board)
def get_width(board):
    board_list = []
    board_list.append(board)
    width = len(board[0])
    return (width)
def is_valid_column(board, column_name):
    width = int(get_width(board))
    if column_name == '':
        return False
    column_name = int(column_name)
    if 0 <= column_name < width:  # Change the condition
        return True
    else:
        return False
def next_player(current_player):
    if current_player == "O":
        return("X")
    elif current_player == "X":
        return("O")
def play_turn(board, player):
  prompt = "Player {} -- enter the column: ".format(player)
  while True:
    column = input(prompt)
    if column.isdigit() and 0 <= int(column) < len(board[0]):
      return int(column)
    elif column == "quit":
      return None

def play_game(board):
    players = ("X")
    i = True
    while i == True:
        display_board(board)
        a = play_turn(board, players)
        if a == None:
            print(f"Result: player {players} quits!")
            i = False
        else:
            players = next_player(players)




# Test Case
board = create_board(7, 6)
play_game(board)
