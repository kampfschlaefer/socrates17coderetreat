import pytest

DEAD = 0
ALIVE = 1


def is_alive(neighbour_count):
    return neighbour_count in [2, 3]


def count_alive_neighbours(neighbours):
    return sum(neighbours)


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
