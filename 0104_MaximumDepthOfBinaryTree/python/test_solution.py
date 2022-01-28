from typing import Optional

import pytest

from solution import Solution, TreeNode


def build_tree(tree: list[int]) -> Optional[TreeNode]:
    tree = [TreeNode(val=v) for v in tree]
    tree_size = len(tree)

    for i, parent in enumerate(tree):
        left_child = 2*i +1
        right_child = 2*i + 2
        if left_child < tree_size:
            parent.left = tree[left_child] if tree[left_child] else None
        if right_child < tree_size:
            parent.right = tree[right_child] if tree[right_child] else None
    
    if tree:
        return tree[0]
    else:
        return None

test_cases = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
]

@pytest.mark.parametrize("tree,expected", test_cases)
def test_maxDepth(tree, expected):
    root = build_tree(tree)
    got = Solution().maxDepth(root)
    assert got == expected


@pytest.mark.parametrize("tree,expected", test_cases)
def test_bfs_traversal(tree, expected):
    root = build_tree(tree)
    got = Solution().bfs_traversal(root)
    assert got == expected
