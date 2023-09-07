def display_board(board):
    # Determine the width and height of the board
    width = len(board[0])
    height = len(board)

    # Print the board rows
    for row in reversed(board):  # Start from the top row
        print
        
        
        print("|", end="")  # Left edge of the board
        for cell in row:
            print(cell, end=" ")  # Print the cell value with a space
        print("|")  # Right edge of the board
    # Print the bottom row with hyphens
    print("|" + "-" * (width * 2) + "|")
    # Print the column labels
    print("|", end="")
    for column in range(width):
        print(column, end=" ")  # Print the column label
    print("|")


display_board(['....', '....', '....', '....'])
