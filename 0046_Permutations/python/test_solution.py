import pytest

import solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_initial_pass(nums, expected):
    got = solution.initial_pass(nums)
    assert len(got) == len(expected)
    for p in got:
        assert list(p) in expected
