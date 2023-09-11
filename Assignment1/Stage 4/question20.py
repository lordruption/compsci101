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
def is_valid_column(board, column_name):
    width = int(get_width(board))
    if column_name == '':
        return False
    column_name = int(column_name)
    if 0 <= column_name < width: 
        return True
    else:
        return False
def next_player(current_player):
    if current_player == "O":
        return("X")
    elif current_player == "X":
        return("O")
def stage_2(width, height):
    board = create_board(width, height)
    play_game(board)
def is_valid_move(board, column_name):
    if not is_valid_column(board, column_name):
        return False
    column_name_int = int(column_name)
    for row in board:
        if row[column_name_int] == '.':
            return True
    else:
        return False
def column_contents(board, column_index):
    result = []
    for row in board:
        result.append(row[column_index])
    result_formatted = ''.join(result)
    return result_formatted
def get_free_row(board, column_index):
    for row_index in range(len(board)):
        if board[row_index][column_index] == '.':
            return row_index
    return -1
def modify_board(board, column_index, row_index, player):
    row_list = list(board[row_index])
    row_list[column_index] = player
    board[row_index] = ''.join(row_list)
def add_piece_to_column(board, player, column_name):
    column_index = int(column_name)
    row_index = get_free_row(board, column_index)
    modify_board(board, column_index, row_index, player)
def play_turn(board, player):
    while True:
        column = input(f"Player {player} -- enter the column: ")
        if column == 'quit':
            return 'quit'
        elif column.isdigit():
            column_index = int(column)
            if 0 <= column_index < len(board[0]) and is_valid_move(board, column_index):
                add_piece_to_column(board, player, column_index)
                return str(column_index)
def stage_3(width, height):
    board = create_board(width, height)
    play_game(board)
def is_full(board):
    for column_index in range(len(board[0])):
        if is_valid_move(board, column_index):
            return False
    return True
def is_winner(board, player):
    for row in board:
        if f"{player * 4}" in row:
            return True
    for col_index in range(len(board[0])):
        column = column_contents(board, col_index)
        if f"{player * 4}" in column:
            return True
    return False
def play_game(board):
    player = ("X")
    i = True
    while i == True:
        display_board(board)
        user_move = play_turn(board, player)
        if user_move == "quit":
            display_board(board)
            print(f"Result: player {player} quits!")
            i = False
        elif is_full(board) == True:
            display_board(board)
            print("Result: draw")
            i = False
        elif is_winner(board, player) == True:
            display_board(board)
            print(f"Result: player {player} wins!")
            i = False
        else:
            player = next_player(player)
            i = True
def stage_4(width, height):
    stage_2(width, height)

# Test case
stage_4(7, 4)