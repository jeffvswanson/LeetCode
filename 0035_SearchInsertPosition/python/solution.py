"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Examples
--------
Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Example 4:
    Input: nums = [1,3,5,6], target = 0
    Output: 0

Example 5:
    Input: nums = [1], target = 0
    Output: 0

Constraints
-----------
* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums contains distinct values sorted in ascending order.
* -104 <= target <= 104
"""


def initial_pass(nums: list[int], target: int) -> int:
    lo_index = 0
    hi_index = len(nums) - 1
    index = -1

    while lo_index <= hi_index:
        mid_index = (lo_index + hi_index) // 2
        if nums[mid_index] == target:
            index = mid_index
            break
        elif nums[mid_index] < target:
            lo_index = mid_index + 1
        else:
            hi_index = mid_index - 1

    if lo_index > hi_index:
        index = lo_index
    return index


def optimized_pass(nums: list[int], target: int) -> int:
    lo_index = 0
    hi_index = len(nums) - 1

    while lo_index <= hi_index:
        mid_index = (lo_index + hi_index) // 2
        if nums[mid_index] > target:
            hi_index = mid_index - 1
        elif nums[mid_index] < target:
            lo_index = mid_index + 1
        else:
            return mid_index
    return lo_index
