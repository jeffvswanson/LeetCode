import pytest

import solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0,1,0,3,12],[1,3,12,0,0]),
        ([0],[0]),
        ([1, 0, 3, 5, 0], [1, 3, 5, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ],
)
def test_initial_pass(nums, expected):
    solution.initial_pass(nums)
    assert nums == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0,1,0,3,12],[1,3,12,0,0]),
        ([0],[0]),
        ([1, 0, 3, 5, 0], [1, 3, 5, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ],
)
def test_optimized_pass(nums, expected):
    solution.optimized_pass(nums)
    assert nums == expected
