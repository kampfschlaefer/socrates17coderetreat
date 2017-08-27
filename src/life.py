def game_of_life(board):
    next_board = [
                  [ 0 for x in line ]
                  for line in board
                 ]
    for row in range(len(board)):
        for col in range(len(row)):
            next_board[row][col] = cell_lives()

    return next_board
