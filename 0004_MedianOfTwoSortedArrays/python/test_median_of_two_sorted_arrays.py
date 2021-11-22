import pytest

import median_of_two_sorted_arrays


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0),
        ([], [1], 1),
        ([2], [], 2),
    ],
)
def test_initial_solution(nums1, nums2, expected):
    got = median_of_two_sorted_arrays.initial_solution(nums1, nums2)
    assert got == expected
