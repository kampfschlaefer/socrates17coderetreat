"""
import pytest
from life import game_of_life

@pytest.mark.parametrize(
    "board,expected_board",
    (
        ([], []),
        ([[0]], [[0]]),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        # One living cell in the middle, it dies
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        # All cells live, all cells die
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        # blinker
        ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
        # blinker 2
        ([[0, 0, 0], [1, 1, 1], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]]),
    )
)
def test_game(board,expected_board):
    next_board = game_of_life(board)
    assert board.__class__ is next_board.__class__
    assert next_board == expected_board
    """
