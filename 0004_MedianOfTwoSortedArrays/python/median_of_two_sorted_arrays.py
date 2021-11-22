"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

For example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""


def initial_solution(nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()

    median = None
    median_index = len(nums1) // 2
    if len(nums1) % 2:  # list length is odd [0, 1, 2]
        median = nums1[median_index]
    else:  # list length is even [0, 1]
        median = (nums1[median_index] + nums1[median_index - 1]) / 2
    return median
