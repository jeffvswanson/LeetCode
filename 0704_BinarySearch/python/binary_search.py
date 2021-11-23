"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints
-----------
* 1 <= nums.length <= 104
* -104 < nums[i], target < 104
* All the integers in nums are unique.
* nums is sorted in ascending order.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


def initial_solution(nums: list[int], target: int) -> int:
    target_index = -1
    lo_index = 0
    hi_index = len(nums) - 1

    while lo_index <= hi_index:
        mid_index = (lo_index + hi_index) // 2
        if target == nums[mid_index]:
            target_index = mid_index
            break
        if target < nums[mid_index]:
            hi_index = mid_index - 1
        else:
            lo_index = mid_index + 1

    return target_index
