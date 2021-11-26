"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Examples
--------
Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints
-----------
* 1 <= s.length <= 105
* s[i] is a printable ascii character.
"""


def initial_solution(s: list[str]):
    if len(s) > 1:
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            s[left_index], s[right_index] = s[right_index], s[left_index]
            left_index += 1
            right_index -= 1


def built_in_solution(s: list[str]):
    s.reverse()
