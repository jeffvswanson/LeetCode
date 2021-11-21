import pytest

import add_two

@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
    ],
)
def test_first_try(l1, l2, expected):
    assert add_two.first_try(l1=l1, l2=l2) == expected

@pytest.mark.parametrize(
    "ints,expected",
    [
        ([2, 4, 3], 342),
        ([0], 0),
        ([9,9,9,9,9,9,9], 9999999),
    ],
)
def test_construct_addend(ints, expected):
    assert add_two.construct_addend(ints=ints) == expected


@pytest.mark.parametrize(
    "num,expected",
    [
        (708, [8, 0, 7]),
        (0, [0]),
        (10009998, [8,9,9,9,0,0,0,1])
    ]
)
def test_deconstruct_num(num, expected):
    got = add_two.deconstruct_num(num=num)
    assert got == expected
