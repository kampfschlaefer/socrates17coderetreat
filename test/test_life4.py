import pytest


def is_alive(neighbour_count):
    return neighbour_count in [2, 3]


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
