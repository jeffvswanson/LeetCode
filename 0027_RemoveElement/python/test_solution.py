import pytest

import solution


@pytest.mark.parametrize(
    "nums,val,expected",
    [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ([1, 1, 1], 2, 3),
        ([2, 2, 2], 2, 0),
        ([], 2, 0),
    ],
)
def test_initial_pass(nums, val, expected):
    got = solution.initial_pass(nums, val)
    assert got == expected
    for i in range(expected):
        assert nums[i] != val
