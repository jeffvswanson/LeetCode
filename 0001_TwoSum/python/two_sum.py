"""
1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
2. You may assume that each input would have exactly one solution, and you may not use the same element twice.
3. You can return the answer in any order.
"""


def brute_force(*, nums: list[int], target: int) -> list[int]:
    indices = set()
    for i, num in enumerate(nums):
        start = i + 1
        nums2 = nums[start:]
        for j, num2 in enumerate(nums2):
            if num + num2 == target:
                indices.add(i)
                indices.add(j + start)
    return list(indices)
