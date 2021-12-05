import pytest

import solution


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (4, 2, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]),
        (1, 1, [[1]]),
    ]
)
def test_initial_pass(n, k, expected):
    got = solution.initial_pass(n, k)
    assert len(got) == len(expected)