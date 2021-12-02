from typing import Optional

import pytest

import solution
from solution import Node


def convert_list_to_binary_search_tree(raw_list: Optional[list[int]]) -> Optional[Node]:
    if not raw_list:
        return None
    root = Node(raw_list[0])
    root.right = convert_list_to_binary_search_tree(raw_list[1:])
    root.left = convert_list_to_binary_search_tree(raw_list[2:])

    return root


@pytest.mark.parametrize(
    "root",
    [([1,2,3,4,5,6,7],[1,None,2,3,None,4,5,6,7,None]), ([], [])],
)
def test_first_pass(root, expected):
    root = convert_list_to_binary_search_tree(root)
    assert root.val == expected[0]
