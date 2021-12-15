import pytest

from solution import ListNode, Solution


def build_linked_list(raw_list: list) -> ListNode:
    root = ListNode(raw_list[0])
    node = root

    for i, val in enumerate(raw_list):
        if i + 1 >= len(raw_list):
            node.next = None
            break

        node.next = ListNode(val=raw_list[i + 1])
        node = node.next

    return root


test_cases = [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
    ([1], [1]),
    ([2, 1, 2, 2, 3], [1, 2, 2, 2, 3]),
    ([1, 1], [1, 1]),
]


@pytest.mark.parametrize("given,expected", test_cases)
def test_insertionSortList(given, expected):
    given_root = build_linked_list(given)
    expected = build_linked_list(expected)

    got = Solution().insertionSortList(given_root)
    while got and expected:
        assert got.val == expected.val
        expected = expected.next
        got = got.next

    # We should be at the end of the linked list and both should be None
    assert got is expected
