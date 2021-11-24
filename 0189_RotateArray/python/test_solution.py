import pytest

import solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([5, 4, 3, 2, 1], 0, [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4], 6, [3, 4, 1, 2]),
        ([1], 4, [1]),
    ],
)
def test_initial_pass(nums, k, expected):
    solution.initial_pass(nums, k)
    assert nums == expected
