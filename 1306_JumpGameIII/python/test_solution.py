import pytest

import solution


@pytest.mark.parametrize(
    "arr,start,expected",
    [
        ([4, 2, 3, 0, 3, 1, 2], 5, True),
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        ([3, 0, 2, 1, 2], 2, False),
        ([1, 1, 1, 1], 3, False),
    ],
)
def test_initial_pass(arr, start, expected):
    got = solution.initial_pass(arr, start)
    assert got is expected
