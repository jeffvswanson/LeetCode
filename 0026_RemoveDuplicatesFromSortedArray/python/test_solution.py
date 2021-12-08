import pytest

import solution


@pytest.mark.parametrize(
    "nums,expected_list,expected_k",
    [
        ([1, 1, 2], [1, 2, 0], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, 0, 0, 0, 0, 0], 5),
        ([], [], 0),
        ([1], [1], 1),
        ([1, 1], [1, 1], 1),
        ([1, 2], [1, 2], 2),
        ([1, 1, 1], [1, 1, 1], 1),
        ([-1, 0, 0, 0, 0, 3, 3], [-1, 0, 3], 3),
    ],
)
def test_initial_pass(nums, expected_list, expected_k):
    got = solution.initial_pass(nums)
    assert got == expected_k
    for i in range(expected_k):
        assert nums[i] == expected_list[i]


@pytest.mark.parametrize(
    "nums,expected_list,expected_k",
    [
        ([1, 1, 2], [1, 2, 0], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, 0, 0, 0, 0, 0], 5),
        ([], [], 0),
        ([1], [1], 1),
        ([1, 1], [1, 1], 1),
        ([1, 2], [1, 2], 2),
        ([1, 1, 1], [1, 1, 1], 1),
        ([-1, 0, 0, 0, 0, 3, 3], [-1, 0, 3], 3),
    ],
)
def test_iterative_pass(nums, expected_list, expected_k):
    got = solution.iterative_pass(nums)
    assert got == expected_k
    for i in range(expected_k):
        assert nums[i] == expected_list[i]
