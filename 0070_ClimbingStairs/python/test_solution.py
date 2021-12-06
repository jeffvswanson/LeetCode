import pytest

import solution


@pytest.mark.parametrize("n,expected", [(2, 2), (3, 3)])
def test_initial_pass(n, expected):
    got = solution.initial_pass(n)
    assert got == expected
