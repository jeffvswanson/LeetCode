from typing import Optional

import pytest

import solution
from solution import ListNode


def create_linked_list(raw_list: list[int]) -> Optional[ListNode]:
    if not raw_list:
        return None
    head = ListNode(val=raw_list[0])
    node = head

    for i, _ in enumerate(raw_list):
        if i + 1 < len(raw_list):
            node.next = ListNode(val=raw_list[i + 1])
            node = node.next

    return head


@pytest.mark.parametrize(
    "given,expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_recursive(given, expected):
    given = create_linked_list(given)
    expected = create_linked_list(expected)
    got = solution.recursive(given)
    if expected:
        while expected:
            assert got.val == expected.val
            expected = expected.next
            got = got.next
    else:
        assert got is expected
