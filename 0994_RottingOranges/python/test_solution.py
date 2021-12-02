import pytest

import solution


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ],
)
def test_first_pass(grid, expected):
    got = solution.first_pass(grid)
    assert got == expected
