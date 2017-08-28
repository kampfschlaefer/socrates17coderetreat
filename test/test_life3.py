"""
No returns!!!
"""
import pytest

def single_cell_step(next_board, current_board, x, y):
    alive_count = 0
    for i in range(x-1, x+2):
        if i >= len(current_board):
            i = 0
        for j in range(y-1, y+2):
            if j >= len(current_board[i]):
                j = 0
            alive_count += current_board[i][j]
    alive_count -= current_board[x][y]
    print("Alive count:", alive_count)

    if alive_count in [2, 3]:
        next_board[x][y] = 1


def game_of_life(current_board, next_board):
    for i in range(len(current_board)):
        for j in range(len(current_board[i])):
            single_cell_step(next_board, current_board, i, j)

@pytest.mark.parametrize(
    "current_board, expected_board, x, y",
    (
        (
            [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            1, 1
        ),
        (
            [
                [ 0, 0, 0, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 0, 0, 0 ],
            ],
            [
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
            ],
            1, 0
        ),
        (
            [
                [ 0, 0, 0, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 0, 0, 0 ],
            ],
            [
                [ 0, 0, 0, 0 ],
                [ 0, 1, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
            ],
            1, 1
        ),
    )
)
def test_single_cell_step(current_board, expected_board, x, y):
    next_board = [
        [ 0 for _ in range(len(current_board[i])) ]
        for i in range(len(current_board))
    ]
    single_cell_step(next_board, current_board, x, y)
    assert next_board == expected_board

@pytest.mark.parametrize(
    "current_board, expected_board",
    (
        (
            [
                [ 0 for _ in range(10) ]
                for _ in range(10)
            ],
            [
                [ 0 for _ in range(10) ]
                for _ in range(10)
            ]
        ),
        (
            [
                [ 0, 0, 0, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 0, 0, 0 ],
            ],
            [
                [ 0, 0, 0, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 1, 1, 0 ],
                [ 0, 0, 0, 0 ],
            ]
        ),
#        (  # Blinker 1
#            [
#                [ 0, 0, 0, 0, 0],
#                [ 0, 0, 1, 0, 0],
#                [ 0, 0, 1, 0, 0],
#                [ 0, 0, 1, 0, 0],
#                [ 0, 0, 0, 0, 0],
#            ],
#            [
#                [ 0, 0, 0, 0, 0],
#                [ 0, 0, 0, 0, 0],
#                [ 0, 1, 1, 1, 0],
#                [ 0, 0, 0, 0, 0],
#                [ 0, 0, 0, 0, 0],
#            ],
#        )
    )
)
def test_game_of_life(current_board, expected_board):
    next_board = [
        [ 0 for _ in range(len(current_board[i])) ]
        for i in range(len(current_board))
    ]

    game_of_life(current_board, next_board)
    assert next_board == expected_board

