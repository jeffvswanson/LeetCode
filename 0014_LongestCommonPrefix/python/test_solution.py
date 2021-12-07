import pytest

import solution


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["flight", "slight", "right"], ""),
    ],
)
def test_initial_pass(strs, expected):
    got = solution.initial_pass(strs)
    assert got == expected


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["flight", "slight", "right"], ""),
    ],
)
def test_faster(strs, expected):
    got = solution.faster(strs)
    assert got == expected
