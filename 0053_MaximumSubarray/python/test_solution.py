import pytest

import solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
    ]
)
def test_initial_pass(nums, expected):
    got = solution.initial_pass(nums)
    assert got == expected
