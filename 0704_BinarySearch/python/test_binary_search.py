import pytest

import binary_search


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([], 3, -1),
        ([5], 5, 0),
        ([5], 1, -1),
    ],
)
def test_initial_solution(nums, target, expected):
    got = binary_search.initial_solution(nums, target)
    assert got == expected
