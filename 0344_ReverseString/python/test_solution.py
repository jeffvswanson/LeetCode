import pytest

import solution


@pytest.mark.parametrize(
    "s,expected",
    [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        (["h"], ["h"]),
    ],
)
def test_initial_solution(s, expected):
    solution.initial_solution(s)
    assert s == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        (["h"], ["h"]),
    ],
)
def test_built_in_solution(s, expected):
    solution.built_in_solution(s)
    assert s == expected
