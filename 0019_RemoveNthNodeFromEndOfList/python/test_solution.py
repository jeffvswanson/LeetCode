import pytest

import solution


def create_linked_list(raw_list) -> solution.ListNode:
    for i, val in enumerate(raw_list):
        if i == 0:
            node = solution.ListNode(val=val)
            head = node
        if i + 1 < len(raw_list):
            node.next = solution.ListNode(val=raw_list[i+1])
        node = node.next
    return head

@pytest.mark.parametrize(
    "raw_list,n,expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, None),
        ([1, 2], 1, [1]),
    ]
)
def test_initial_pass(raw_list, n, expected):
    head = create_linked_list(raw_list)
    got = solution.initial_pass(head, n)

    if expected:
        expected = create_linked_list(expected)
    if got and expected:
        while got.val and expected.val:
            assert got.val == expected.val
            got = got.next
            expected = expected.next
            if got is None:
                assert expected is None
                break
    else:
        assert got is None
