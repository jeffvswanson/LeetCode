import pytest

import length_of_longest_substring

@pytest.mark.parametrize(
    "s,expected",
    [
        ("abcabcbb",3),
        ("bbbbb", 1),
        ('pwwkew', 3),
        ('', 0),
    ],
)
def test_len_longest_substring(s, expected):
    got = length_of_longest_substring.len_longest_substring(s)
    assert got == expected
