import pytest

import solution


@pytest.mark.parametrize(
    "image,starting_row_index,starting_column_index,new_color,expected",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),
        ([[1]], 0, 0, 2, [[2]]),
        ([[1, 1], [1, 0]], 0, 0, 1, [[1, 1], [1, 0]]),
    ],
)
def test_initial_solution(image, starting_row_index, starting_column_index, expected, new_color):
    got = solution.initial_pass(image, starting_row_index, starting_column_index, new_color)
    assert got == expected
