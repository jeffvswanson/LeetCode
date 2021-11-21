"""
Given a string s, find the length of the longest substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def len_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring in s without repeating characters.

    Args:
        s (str): Given string.

    Returns:
        int: Length of the longest substring in s without repeating characters.
    
    Speed Analysis: O(n), no matter how you implement this algorithm, all of the characters will need to be checked.
    Memory Analysis: O(n), the initial string is going to be the largest memory element with a possible substring as
    large as the initial string, but no greater than that.
    """
    substring = set()
    max_len = 0
    i = 0
    while s:
        char = s[i]
        if char not in substring:
            substring.add(char)
            i += 1
            if i >= len(s):
                max_len = max(max_len, len(substring))
                break
            continue
        else:
            max_len = max(max_len, len(substring))
            s = s[1:]
            if max_len > len(s):
                break
            substring = set()
            i = 0
    return max_len
