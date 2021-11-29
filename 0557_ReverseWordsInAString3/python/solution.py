"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
initial word order.

Examples
--------
Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
    Input: s = "God Ding"
    Output: "doG gniD"

Constraints
-----------
* 1 <= s.length <= 5 * 104
* s contains printable ASCII characters.
* s does not contain any leading or trailing spaces.
* There is at least one word in s.
* All the words in s are separated by a single space.
"""


def initial_solution(s: str) -> str:
    split_s = [list(word) for word in s.split()]
    for word in split_s:
        word.reverse()
    split_s = ["".join(word) for word in split_s]
    reversed_s = " ".join(split_s)
    return reversed_s


def faster_solution(s: str) -> str:
    split_s = s.split(" ")
    for i in range(len(split_s)):
        split_s[i] = split_s[i][::-1]
    return " ".join(split_s)
