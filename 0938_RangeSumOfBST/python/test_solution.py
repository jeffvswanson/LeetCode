from typing import Optional

import pytest

import solution
from solution import TreeNode


def build_tree(root: Optional[TreeNode], val: Optional[int]) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    if not val:
        return None
    if val < root.val:
        root.left = build_tree(root.left, val)
    else:
        root.right = build_tree(root.right, val)

    return root


test_cases = [
    ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
    ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
    ([2], 1, 3, 2),
    ([1], 2, 3, 0),
]


@pytest.mark.parametrize("given,low,high,expected", test_cases)
def test_initial_pass(given, low, high, expected):
    root = None
    for i, val in enumerate(given):
        if i == 0:
            root = build_tree(root, val=val)
        else:
            build_tree(root, val)

    got = solution.initial_pass(root, low, high)
    assert got == expected


@pytest.mark.parametrize("given,low,high,expected", test_cases)
def test_optimized_pass(given, low, high, expected):
    root = None
    for i, val in enumerate(given):
        if i == 0:
            root = build_tree(root, val=val)
        else:
            build_tree(root, val)

    got = solution.optimized_pass(root, low, high)
    assert got == expected
