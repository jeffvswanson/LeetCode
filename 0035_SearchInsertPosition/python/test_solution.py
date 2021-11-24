import pytest

import solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ],
)
def test_initial_pass(nums, target, expected):
    got = solution.initial_pass(nums, target)
    assert got == expected


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ],
)
def test_optimized_pass(nums, target, expected):
    got = solution.optimized_pass(nums, target)
    assert got == expected
