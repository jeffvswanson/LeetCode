import pytest

import solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_first_pass(nums, expected):
    got = solution.first_pass(nums)
    assert got == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_one_line_pass(nums, expected):
    got = solution.one_line_pass(nums)
    assert got == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_optimized_pass(nums, expected):
    got = solution.optimized_pass(nums)
    assert got == expected
