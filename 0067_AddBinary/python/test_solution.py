import pytest

from solution import Solution


test_cases = [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
]


@pytest.mark.parametrize("a,b,expected", test_cases)
def test_initial_pass(a, b, expected):
    got = Solution().addBinary(a, b)
    assert got == expected
