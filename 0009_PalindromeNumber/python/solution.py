"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121
is palindrome while 123 is not.

Examples
--------
Example 1:
    Input: x = 121
    Output: true

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
    Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
    Input: x = -101
    Output: false

Constraints
-----------
-231 <= x <= 231 - 1
"""


def initial_pass(x: int) -> bool:
    if x < 0:
        return False

    is_palindrome = True
    s = str(x)
    left_index, right_index = 0, len(s) - 1
    while left_index <= right_index:
        if s[left_index] != s[right_index]:
            is_palindrome = False
            break
        left_index += 1
        right_index -= 1
    return is_palindrome


def one_liner(x: int) -> bool:
    return str(x) == str(x)[::-1]
