import pytest

import solution


@pytest.mark.parametrize(
    "mat,expected",
    [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    ],
)
def test_first_pass(mat, expected):
    got = solution.first_pass(mat)
    assert got == expected
