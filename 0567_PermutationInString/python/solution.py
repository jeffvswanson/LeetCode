"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Examples
--------
Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Constraints
-----------
* 1 <= s1.length, s2.length <= 104
* s1 and s2 consist of lowercase English letters.
"""
from collections import Counter

def initial_pass(s1: str, s2: str) -> bool:
    # Store the frequency of characters in the first string
    s1_character_frequency = Counter(s1)
    s2_character_frequency = Counter(s2)

    contains_permutation = False
    for key, value in s1_character_frequency.items():
        if key not in s2_character_frequency:
            return contains_permutation
        elif s2_character_frequency[key] < value:
            return contains_permutation
    
    def check_for_permutation(s1_character_frequency, s2):
        start_permutation = 0
        contains_permutation = False
        # When a possible character is found, move the start_permutation pointer
        # Then look at the next set of letters within the length of the string, s1
        # Otherwise, move the start_permutation to the index position in string, s2, after the search
        while start_permutation <= len(s2) - len(s1):
            if s2[start_permutation] in s1_character_frequency:
                possible_permutation = Counter(s2[start_permutation:start_permutation+len(s1)])
                if possible_permutation == s1_character_frequency:
                    contains_permutation = True
                    break
            start_permutation += 1
        return contains_permutation

    return check_for_permutation(s1_character_frequency, s2)

