import pytest

import solution


def create_linked_list(raw_list: list) -> solution.ListNode:
    for i, val in enumerate(raw_list):
        if not i:
            node = solution.ListNode(val=val)
            head = node
        if i + 1 < len(raw_list):
            node.next = solution.ListNode(raw_list[i+1])
        node = node.next
    return head


@pytest.mark.parametrize(
    "raw_list,expected",
    [
        ([1,2,3,4,5],[3,4,5]),
        ([1,2,3,4,5,6],[4,5,6]),
    ],
)
def test_initial_pass(raw_list,expected):
    head = create_linked_list(raw_list)
    got = solution.initial_pass(head)
    expected = create_linked_list(expected)
    while got.next and expected.next:
        assert got.val == expected.val
        got = got.next
        expected = expected.next


@pytest.mark.parametrize(
    "raw_list,expected",
    [
        ([1,2,3,4,5],[3,4,5]),
        ([1,2,3,4,5,6],[4,5,6]),
    ],
)
def test_faster_solution(raw_list,expected):
    head = create_linked_list(raw_list)
    got = solution.faster_solution(head)
    expected = create_linked_list(expected)
    while got.next and expected.next:
        assert got.val == expected.val
        got = got.next
        expected = expected.next
