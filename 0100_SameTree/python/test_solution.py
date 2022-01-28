from typing import Optional

import pytest

from solution import Solution, TreeNode


def build_tree(tree: Optional[list[int]]) -> Optional[TreeNode]:
    tree = [TreeNode(val=v) for v in tree]
    tree_size = len(tree)

    for i, parent in enumerate(tree):
        left = 2*i + 1
        if left < tree_size:
            parent.left = tree[left] if tree[left] is not None else None
        right = 2*i + 2
        if right < tree_size:
            parent.right = tree[right] if tree[right] is not None else None
    
    return tree[0] if tree else tree
        


test_cases = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1], [], False),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([], [], True),
    ([1], [2], False),
]


@pytest.mark.parametrize("p,q,expected", test_cases)
def test_isSameTree(p, q, expected):
    p = build_tree(p)
    q = build_tree(q)
    got = Solution().isSameTree(p, q)
    assert got is expected


@pytest.mark.parametrize("p,q,expected", test_cases)
def test_iterative(p, q, expected):
    p = build_tree(p)
    q = build_tree(q)
    got = Solution().iterative(p, q)
    assert got is expected
