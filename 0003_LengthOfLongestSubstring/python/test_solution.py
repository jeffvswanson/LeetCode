import pytest

import solution

@pytest.mark.parametrize(
    "s,expected",
    [
        ("abcabcbb",3),
        ("bbbbb", 1),
        ('pwwkew', 3),
        ('', 0),
        (' ', 1),
        ("abcabcbbd",3),
        ('au', 2),
        ('abba', 2),
        ('dvdf', 3),
        ('tmmzuxt', 5),
    ],
)
def test_brute_force(s, expected):
    got = solution.brute_force(s)
    assert got == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abcabcbb",3),
        ("bbbbb", 1),
        ('pwwkew', 3),
        ('', 0),
        (' ', 1),
        ("abcabcbbd",3),
        ('au', 2),
        ('abba', 2),
        ('dvdf', 3),
        ('tmmzuxt', 5),
    ],
)
def test_sliding_window(s, expected):
    got = solution.sliding_window(s)
    assert got == expected
