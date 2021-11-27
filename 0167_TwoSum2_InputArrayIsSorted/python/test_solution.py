import pytest

import solution


@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0],-1,[1,2])
    ],
)
def test_initial_pass(numbers, target, expected):
    got = solution.initial_pass(numbers, target)
    assert got == expected


@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0],-1,[1,2])
    ],
)
def test_two_pointer_pass(numbers, target, expected):
    got = solution.two_pointer_pass(numbers, target)
    assert got == expected


@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0],-1,[1,2])
    ],
)
def test_dict_solution(numbers, target, expected):
    got = solution.dict_solution(numbers, target)
    assert got == expected
