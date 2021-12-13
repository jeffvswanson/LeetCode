import pytest

import solution

test_cases = [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("triplepillooooow", 5),
    ("hooraaaaaaaaaaay", 11),
    ("tourist", 1),
    ("cc", 2),
]


@pytest.mark.parametrize("s,expected", test_cases)
def test_initial_pass(s, expected):
    got = solution.initial_pass(s)
    assert got == expected


@pytest.mark.parametrize("s,expected", test_cases)
def test_optimized_pass(s, expected):
    got = solution.optimized_pass(s)
    assert got == expected
