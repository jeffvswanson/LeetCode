"""
1446. Consecutive Characters

The power of the string is the maximum length of a non-empty substring that contains
only one unique character.

Given a string s, return the power of s.

Examples
-------- 
Example 1:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
    Input: s = "abbcccddddeeeeedcba"
    Output: 5
    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
    Input: s = "triplepillooooow"
    Output: 5

Example 4:
    Input: s = "hooraaaaaaaaaaay"
    Output: 11

Example 5:
    Input: s = "tourist"
    Output: 1

Constraints
-----------
* 1 <= s.length <= 500
* s consists of only lowercase English letters.
"""


def initial_pass(s: str) -> int:
    char_pows = {}  # character: sequential appearances

    left_index, right_index = 0, 0
    while right_index < len(s):
        if s[right_index] not in char_pows:
            char_pows[s[right_index]] = 1
        if s[right_index] != s[right_index - 1]:
            char_pows[s[left_index]] = max(
                right_index - left_index, char_pows[s[left_index]]
            )
            left_index = right_index
        elif right_index + 1 == len(s):
            char_pows[s[left_index]] = max(
                len(s) - left_index, char_pows[s[left_index]]
            )
        right_index += 1

    return max(char_pows.values())


def optimized_pass(s: str) -> int:
    power = [1 for _ in s]
    char = s[0]
    for i in range(1, len(s)):
        if char != s[i]:
            char = s[i]
        else:
            power[i] += power[i - 1]
    return max(power)
