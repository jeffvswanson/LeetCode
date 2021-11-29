import pytest

import solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
        ("h", "h"),
    ],
)
def test_initial_solution(s, expected):
    got = solution.initial_solution(s)
    assert got == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
        ("h", "h"),
    ],
)
def test_faster_solution(s, expected):
    got = solution.faster_solution(s)
    assert got == expected
