from typing import Optional

import pytest

import solution
from solution import ListNode


def create_linked_list(raw_list: list) -> Optional[ListNode]:
    if not raw_list:
        return None

    head = ListNode(val=raw_list[0])
    node = head
    for i, _ in enumerate(raw_list):
        if i + 1 < len(raw_list):
            node.next = ListNode(raw_list[i + 1])
        node = node.next
    return head


@pytest.mark.parametrize(
    "list1,list2,expected",
    [
        pytest.param([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        pytest.param([], [], []),
        pytest.param([], [0], [0]),
        pytest.param([0], [], [0]),
    ],
)
def test_initial_pass(list1, list2, expected):
    head1 = create_linked_list(list1)
    head2 = create_linked_list(list2)
    expected = create_linked_list(expected)

    got = solution.initial_pass(head1, head2)
    if expected:
        while expected:
            assert got.val == expected.val
            expected = expected.next
            got = got.next
