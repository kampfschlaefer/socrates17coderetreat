import pytest

from functools import reduce

def is_alive(neighbour_count):
    return neighbour_count in [2, 3]

def aliveNeighborCount(neighbors):
    return reduce(lambda c, n: {1: c+1, 0: c}[n], neighbors)

def getNeighbors(board, x, y):
    neighbors = []
    for i in range(x-1, x+2):
        if i >= len(board):
            i = 0
        for j in range(y-1, y+2):
            if j >= len(board[i]):
                j = 0
            if not (i==x and j==y):
                neighbors.append(board[i][j])
    return neighbors

def alive_on_board(board, x, y):
    return is_alive(aliveNeighborCount(getNeighbors(board, x, y)))

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
    "cells, expected_count",
    (
        ([0 for i in range(8)], 0),
        ([1 for i in range(8)], 8),
        ([1 for i in range(4)] + [0 for i in range(4)], 4),
    )
)
def test_alive_neighborcount(cells, expected_count):
    assert aliveNeighborCount(cells) == expected_count

@pytest.mark.parametrize(
    "board, x, y, expected_neighbors",
    (
        ([
            [ 0 for _ in range(3) ]
            for _ in range(3)
        ], 1, 1, [ 0 for _ in range(8) ]),
        ([
            [ 0 for _ in range(3) ]
            for _ in range(3)
        ], 0, 0, [ 0 for _ in range(8) ]),
        ([
            [ 0 for _ in range(3) ]
            for _ in range(3)
        ], 2, 2, [ 0 for _ in range(8) ]),
        ([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], 1, 1, [0, 0, 0, 0, 0, 0, 0, 1]),
        ([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], 1, 2, [0, 0, 0, 1, 0, 0, 1, 0]),
    )
)
def test_get_neighbors(board, x, y, expected_neighbors):
    assert getNeighbors(board, x, y) == expected_neighbors

@pytest.mark.parametrize(
    "board, x, y, expected_neighborcount",
    (
        (
            [ [ 0 for _ in range(5) ] for _ in range(5) ],
            1, 1,
            0
        ),
    )
)
def test_get_alive_neighborcount_from_board(board, x, y, expected_neighborcount):
    assert aliveNeighborCount(getNeighbors(board, x, y)) == expected_neighborcount

@pytest.mark.parametrize(
    "board, x, y, expectAlive",
    (
        (
            [ [ 0 for _ in range(5) ] for _ in range(5) ],
            1, 1,
            False
        ),
        (
            [ [ 1 for _ in range(5) ] for _ in range(5) ],
            1, 1,
            False
        ),
    )
)
def test_is_alive_from_board(board, x, y, expectAlive):
    assert is_alive(aliveNeighborCount(getNeighbors(board, x, y))) == expectAlive

