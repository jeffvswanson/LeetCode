import pytest

import two_sum


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_brute_force(nums, target, expected):
    assert two_sum.brute_force(nums=nums, target=target) == expected
