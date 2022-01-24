from typing import Optional

import pytest

from solution import Solution, TreeNode


def build_tree(tree: list[int]) -> Optional[TreeNode]:
    if not tree:
        return []
    tree = [TreeNode(val=v) for v in tree]
    tree_size = len(tree)
    for i, node in enumerate(tree):
        if 2 * i + 1 < tree_size:
            node.left = tree[2*i + 1]
        if 2 * i + 2 < tree_size:
            node.right = tree[2*i + 2]
        i += 1
    root = tree[0]
    return root


test_cases = [
    ([1, None, 2, 3], [1, 3, 2]),
    ([], []),
    ([1], [1]),
    ([6, 4, None, 3, 5], [6, 3, 4, 5]),
    ([10, 5, 20, 3, 7, 15, 25], [10, 3, 5, 7, 15, 20, 25])
]

@pytest.mark.parametrize("tree,expected", test_cases)
def test_inorderTraversal(tree, expected):
    root = build_tree(tree)
    got = Solution().inorderTraversal(root)
    assert got == expected
