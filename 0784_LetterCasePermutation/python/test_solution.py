import pytest 

import solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("a1b2", ["a1b2","a1B2","A1b2","A1B2"]),
        ("3z4", ["3z4","3Z4"]),
        ("12345", ["12345"]),
        ("0", ["0"]),
        ("A1c3", ["a1c3", "A1c3", "a1C3", "A1C3"]),
    ],
)
def test_initial_pass(s, expected):
    got = solution.initial_pass(s)
    assert len(got) == len(expected)
    for ans in got:
        assert ans in expected
 