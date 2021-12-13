"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one
number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Examples
--------
Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
    Input: nums = [1]
    Output: 1

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints
-----------
* 1 <= nums.length <= 105
* -104 <= nums[i] <= 104
"""

def initial_pass(nums: list[int]) -> int:
    # Check each subarray from size 1 to size n
    max_sum = -105 * 106  # Ensures we start at a value that can be overwritten 
    for i in range(1, len(nums)+1):
        start_index = 0
        end_index = i
        while end_index <= len(nums):
            max_sum = max(max_sum, sum(nums[start_index:end_index]))
            start_index += 1
            end_index += 1

    return max_sum
