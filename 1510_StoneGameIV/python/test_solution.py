import pytest

import solution

test_cases = [
    (1, True),
    (2, False),
    (4, True),
    (8, True),
]

@pytest.mark.parametrize(
    "n,expected", test_cases
)
def test_winnerSquareGame(n, expected):
    got = solution.Solution().winnerSquareGame(n)
    assert got is expected
