import pytest

DEAD = 0
ALIVE = 1


def is_alive(neighbour_count):
    return neighbour_count in [2, 3]


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
Determine whether the cell at (x, y) is alive.
"""
def is_cell_alive(board, x, y):
    return is_alive(get_neighbors(board, x, y))


@pytest.mark.parametrize(
        "neighbour_count, expected_alive",
        (
            (0, False),
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (6, False),
            (7, False),
            (8, False),
        )
)
def test_is_alive(neighbour_count, expected_alive):
    assert is_alive(neighbour_count) == expected_alive


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
        "board, x, y, expected_alive",
        (
            ([[DEAD]*3 for _ in range(3)],
             1, 1,
             False),
            ([[ALIVE]*3 for _ in range(3)],
             1, 1,
             False),
            ([[DEAD, DEAD, DEAD],
              [DEAD, ALIVE, DEAD],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             False),
            ([[DEAD, DEAD, DEAD],
              [DEAD, ALIVE, ALIVE],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             False),
            ([[DEAD, DEAD, DEAD],
              [DEAD, DEAD, ALIVE],
              [DEAD, DEAD, ALIVE]],
             1, 1,
             False),
        )
    )
def test_is_cell_alive(board, x, y, expected_alive):
    assert is_cell_alive(board, x, y) == expected_alive
