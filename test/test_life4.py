import pytest
import random
import time
import sys

DEAD = 0
ALIVE = 1


"""
Return the next state of a cell if it would have the given count of alive neighbours.
"""
def next_state(alive_neighbour_count):
    return ALIVE if alive_neighbour_count in [2, 3] else DEAD


"""
Return the number of neighbours that are alive.
"""
def count_alive_neighbours(neighbours):
    return sum(neighbours)


"""
Get the neighbours for the cell at (x, y).

No wrap-around at the borders!
"""
def get_neighbors(board, x, y):
    neighbours = []
    for i in range(max(0, x-1), min(x+2, len(board))):
        for j in range(max(0, y-1), min(y+2, len(board[i]))):
            if (i, j) != (x, y):
                neighbours.append(board[i][j])
    return neighbours


"""
Determine the next state of the cell at (x, y).
"""
def next_cell_state(board, x, y):
    return next_state(count_alive_neighbours(get_neighbors(board, x, y)))


"""
Based on the given board create the board for the next round.
"""
def create_next_board(board):
    next_board = [[DEAD]*len(row) for row in board]

    for x in range(len(board)):
        for y in range(len(board[x])):
            next_board[x][y] = next_cell_state(board, x, y)

    return next_board


"""
Create a random board if given width and height and fill it with a given amount of alive cells.
"""
def create_random_board(width, height, alive_count):
    board = [[DEAD]*width for _ in range(height)]

    while alive_count > 0:
        x = random.randint(0, height-1)
        y = random.randint(0, width-1)
        if board[x][y] == DEAD:
            board[x][y] = ALIVE
            alive_count -= 1
    return board

"""
Print a board to stdout.
"""
def print_board(board):
    for row in board:
        for cell in row:
            print('#' if cell == ALIVE else ' ', end='')
        print()


"""
Count the number of alive cells in the board.
"""
def alive_cell_count(board):
    return sum(sum(row) for row in board)


"""
Play a game of life.
"""
def play(width, height, fill_rate):
    alive_count = fill_rate * width * height
    board = create_random_board(width, height, alive_count)
    print_board(board)
    while alive_cell_count(board) > 0:
        board = create_next_board(board)
        print_board(board)
        print()
        time.sleep(1)


@pytest.mark.parametrize(
        "neighbour_count, expected_state",
        (
            (0, DEAD),
            (1, DEAD),
            (2, ALIVE),
            (3, ALIVE),
            (4, DEAD),
            (5, DEAD),
            (6, DEAD),
            (7, DEAD),
            (8, DEAD),
        )
)
def test_next_state(neighbour_count, expected_state):
    assert next_state(neighbour_count) == expected_state


@pytest.mark.parametrize(
        "neighbours, expected_alive_count",
        (
            ([DEAD]*8, 0),
            ([ALIVE]*8, 8),
            ([DEAD, ALIVE]*4, 4),
        )
    )
def test_count_alive_neighbours(neighbours, expected_alive_count):
    assert count_alive_neighbours(neighbours) == expected_alive_count


neighbour_test_board = [
                            [DEAD, ALIVE, ALIVE, DEAD],
                            [ALIVE, DEAD, ALIVE, DEAD],
                            [ALIVE, ALIVE, DEAD, DEAD],
                            [DEAD, ALIVE, DEAD, ALIVE]
                        ]
@pytest.mark.parametrize(
        "board, x, y, expected_neighbours",
        (
            ([[DEAD]*10 for _ in range(12)],
             1, 1,
             [DEAD]*8),
            (neighbour_test_board[:],
             1, 1,
             [DEAD, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, DEAD]),
            (neighbour_test_board[:],
             2, 2,
             [DEAD, ALIVE, DEAD, ALIVE, DEAD, ALIVE, DEAD, ALIVE]),
            (neighbour_test_board[:],
             3, 0,
             [ALIVE, ALIVE, ALIVE]),
            (neighbour_test_board[:],
             2, 0,
             [ALIVE, DEAD, ALIVE, DEAD, ALIVE]),
            (neighbour_test_board[:],
             0, 3,
             [ALIVE, ALIVE, DEAD]),
            (neighbour_test_board[:],
             1, 3,
             [ALIVE, DEAD, ALIVE, DEAD, DEAD]),
            (neighbour_test_board[:],
             0, 2,
             [ALIVE, DEAD, DEAD, ALIVE, DEAD]),
        )
    )
def test_get_neighbors(board, x, y, expected_neighbours):
    assert get_neighbors(board, x, y) == expected_neighbours


@pytest.mark.parametrize(
        "board, x, y, expected_state",
        (
            ([[DEAD]*3 for _ in range(3)],
             1, 1,
             DEAD),
            ([[ALIVE]*3 for _ in range(3)],
             1, 1,
             DEAD),
            ([[DEAD, DEAD, DEAD],
              [DEAD, ALIVE, DEAD],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             DEAD),
            ([[DEAD, DEAD, DEAD],
              [DEAD, ALIVE, ALIVE],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             ALIVE),
            ([[DEAD, DEAD, DEAD],
              [DEAD, DEAD, ALIVE],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             ALIVE),
        )
    )
def test_next_cell_state(board, x, y, expected_state):
    assert next_cell_state(board, x, y) == expected_state


@pytest.mark.parametrize(
        "board, expected_next_board",
        (
            ([[DEAD]*10 for _ in range(15)],
             [[DEAD]*10 for _ in range(15)]),
            ([
                 [DEAD, DEAD, DEAD, DEAD, DEAD],
                 [DEAD, DEAD, ALIVE, DEAD, DEAD],
                 [DEAD, DEAD, ALIVE, DEAD, DEAD],
                 [DEAD, DEAD, ALIVE, DEAD, DEAD],
                 [DEAD, DEAD, DEAD, DEAD, DEAD]
             ],
             [
                 [DEAD, DEAD, DEAD, DEAD, DEAD],
                 [DEAD, ALIVE, DEAD, ALIVE, DEAD],
                 [DEAD, ALIVE, ALIVE, ALIVE, DEAD],
                 [DEAD, ALIVE, DEAD, ALIVE, DEAD],
                 [DEAD, DEAD, DEAD, DEAD, DEAD]
             ]),

        )
)
def test_create_next_board(board, expected_next_board):
    assert create_next_board(board) == expected_next_board


@pytest.mark.parametrize(
        "width, height, alive_count",
        (
            (80, 40, 10),
            (80, 40, 20),
            (80, 40, 40),
            (40, 80, 10),
            (40, 80, 30),
            (40, 80, 80),
        )
    )
def test_create_random_board(width, height, alive_count):
    board = create_random_board(width, height, alive_count)
    assert len(board) == height
    for row in board:
        assert len(row) == width
    assert alive_cell_count(board) == alive_count
    print_board(board)

@pytest.mark.parametrize(
        "board, expected_alive_count",
        (
            (
                [[DEAD]*10 for _ in range(10)],
                0
            ),
            (
                [[ALIVE]*10 for _ in range(10)],
                100
            ),
            (
                [
                    [DEAD, DEAD, ALIVE],
                    [ALIVE, DEAD, DEAD],
                    [DEAD, ALIVE, DEAD]
                ],
                3
            ),
        )
    )
def test_alive_cell_count(board, expected_alive_count):
    assert alive_cell_count(board) == expected_alive_count



if __name__ == "__main__":
    assert len(sys.argv) == 4
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    fill_rate = float(sys.argv[3])

    play(width, height, fill_rate)
