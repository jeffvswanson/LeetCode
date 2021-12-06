import pytest

import solution


@pytest.mark.parametrize(
    "x,expected", [(121, True), (-121, False), (10, False), (-101, False), (5, True)]
)
def test_initial_pass(x, expected):
    got = solution.initial_pass(x)
    assert got == expected


@pytest.mark.parametrize(
    "x,expected", [(121, True), (-121, False), (10, False), (-101, False), (5, True)]
)
def test_one_liner(x, expected):
    got = solution.one_liner(x)
    assert got == expected
