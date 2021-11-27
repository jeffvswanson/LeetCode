"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Examples
--------
Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints
-----------
* 2 <= numbers.length <= 3 * 104
* -1000 <= numbers[i] <= 1000
* numbers is sorted in non-decreasing order.
* -1000 <= target <= 1000
* The tests are generated such that there is exactly one solution.
"""

def initial_pass(numbers: list[int], target: int) -> list[int]:
    for i, addend_1 in enumerate(numbers):
        addend_2 = target - addend_1
        if addend_2 in numbers:
            j = numbers.index(addend_2, i+1)
        else:
            continue
        addends = [i+1, j+1]
        break
    return addends


def two_pointer_pass(numbers: list[int], target: int) -> list[int]:
    left_index, right_index = 0, len(numbers) - 1
    while left_index < right_index:
        if numbers[left_index] + numbers[right_index] == target:
            addends = [left_index+1, right_index+1]
            break
        elif numbers[left_index] + numbers[right_index] < target:
            left_index += 1
        else:
            right_index -= 1
    return addends


def dict_solution(numbers: list[int], target: int) -> list[int]:
    possible_addends = {}
    for i, addend_1 in enumerate(numbers):
        if addend_1 in possible_addends:
            addends = [possible_addends[addend_1], i+1]
            break
        possible_addends[target - addend_1] = i+1
    return addends
