def is_valid_column(board, column_name):
    width = int(get_width(board))
    if column_name == '':
        return False
    column_name = int(column_name)
    if 0 <= column_name < width:  # Change the condition
        return True
    else:
        return False
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



#This is a test case
board = create_board(7, 6)
print(is_valid_column(board, ''))
print(is_valid_column(board, '12'))
print(is_valid_column(board, '-1'))
print(is_valid_column(board, '0'))
print(is_valid_column(board, '1'))
print(is_valid_column(board, '2'))
print(is_valid_column(board, '3'))
print(is_valid_column(board, '6'))
print(is_valid_column(board, '7'))
print(is_valid_column(board, '8'))
#board == ['.......', '.......', '.......', '.......', '.......', '.......']
#width = 7