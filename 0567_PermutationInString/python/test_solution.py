import pytest

import solution

@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("a", "b", False),
        ("a", "a", True),
        ("abba", "yabbadabba", True),
        ("abba", "baab", True),
        ("abba", "zabbzbabzabzab", False),
        ("abba", "ab", False),
    ]
)
def test_initial_pass(s1, s2, expected):
    # breakpoint()
    got = solution.initial_pass(s1, s2)
    assert got is expected
