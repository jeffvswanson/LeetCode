"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Examples
--------
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
    Input: s = ""
    Output: 0

Constraints
-----------
* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.

"""

def brute_force(s: str) -> int:
    """
    Finds the length of the longest substring in s without repeating characters.

    Parameters
    ----------
    s : str 
        Given string.

    Returns:
    int
        Length of the longest substring in s without repeating characters.
    
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


def sliding_window(s: str) -> int:
    characters = {}  # key=character, value=index found
    longest_substring, substring_start = 0, 0
    for i, char in enumerate(s):
        if char not in characters:
            longest_substring = max(longest_substring, i - substring_start + 1)
        else:
            if characters[char] < substring_start:
                longest_substring = max(longest_substring, i - substring_start + 1)
            else:
                substring_start = characters[char] + 1
        characters[char] = i
    return longest_substring
