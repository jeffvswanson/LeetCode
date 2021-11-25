"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.
Note that you must do this in-place without making a copy of the array.

Examples
--------
Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints
-----------
* 1 <= nums.length <= 104
* -231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
"""

def initial_pass(nums: list[int]):
    i = 0
    while i < (len(nums) - 1):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1
        i += 1


def optimized_pass(nums: list[int]):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
