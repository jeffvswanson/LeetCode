"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

Examples
--------
Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints
-----------
* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums is sorted in non-decreasing order.
"""


def first_pass(nums: list[int]) -> list[int]:
    for i, v in enumerate(nums):
        nums[i] = v ** 2
    nums = divide_and_conquer(nums)
    return nums


def divide_and_conquer(nums: list[int]) -> list[int]:
    # Base case: if the length of nums is one or empty the list is sorted by default.
    if len(nums) < 2:
        return nums

    lower_half = divide_and_conquer(nums[: len(nums) // 2])
    upper_half = divide_and_conquer(nums[len(nums) // 2 :])

    nums = merge_sort(lower_half, upper_half)
    return nums


def merge_sort(lower_half: list[int], upper_half: list[int]) -> list[int]:
    i, j, k = 0, 0, 0

    merge_list = []
    while k < (len(lower_half) + len(upper_half)):
        # Check if a list is out of elements and copy the rest of the elements left in the other array.
        if i >= len(lower_half):
            while j < len(upper_half):
                merge_list.append(upper_half[j])
                j += 1
                k += 1
            break
        elif j >= len(upper_half):
            while i < len(lower_half):
                merge_list.append(lower_half[i])
                i += 1
                k += 1
            break

        if lower_half[i] <= upper_half[j]:
            merge_list.append(lower_half[i])
            i += 1
        else:
            merge_list.append(upper_half[j])
            j += 1
        k += 1
    return merge_list


def one_line_pass(nums: list[int]) -> list[int]:
    return sorted([num ** 2 for num in nums])


def optimized_pass(nums: list[int]) -> list[int]:
    squared_and_sorted_nums = [None for _ in nums]
    left_index, right_index = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left_index]) > abs(nums[right_index]):
            squared_and_sorted_nums[i] = nums[left_index] ** 2
            left_index += 1
        else:
            squared_and_sorted_nums[i] = nums[right_index] ** 2
            right_index -= 1
    return squared_and_sorted_nums
