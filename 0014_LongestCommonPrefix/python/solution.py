"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Examples
--------
Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints
-----------
* 1 <= strs.length <= 200
* 0 <= strs[i].length <= 200
* strs[i] consists of only lower-case English letters.
"""


def initial_pass(strs: list[str]) -> str:
    common_prefix = strs[0]
    for s in strs:
        # Case 1: string in question is longer than the common prefix
        # Case 2: The character at position i of the common prefix does not match the
        # character at position i of the investigated string
        if len(common_prefix) > len(s):
            common_prefix = common_prefix[: len(s)]
        if common_prefix:
            i = 0
            while i < len(common_prefix):
                if common_prefix[i] != s[i]:
                    common_prefix = common_prefix[:i]
                    break
                i += 1
        else:
            break
    return common_prefix


def faster(strs: list[str]) -> str:
    common_prefix = min(strs, key=len)
    if common_prefix:
        for i, char in enumerate(common_prefix):
            for s in strs:
                if char != s[i]:
                    return common_prefix[:i]
    return common_prefix
