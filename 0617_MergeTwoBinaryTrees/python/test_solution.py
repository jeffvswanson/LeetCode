import pytest

import solution


def root_1a() -> solution.TreeNode:
    root = solution.TreeNode(val=1)
    
    root.left = solution.TreeNode(val=3)
    root.left.left = solution.TreeNode(val=5)
    
    root.right = solution.TreeNode(val=2)

    return root

def root_1b() -> solution.TreeNode:
    root = solution.TreeNode(val=2)
    
    root.left = solution.TreeNode(val=1)
    root.left.right = solution.TreeNode(val=4)\

    root.right = solution.TreeNode(val=3)
    root.right.right = solution.TreeNode(val=7)

    return root

def expected_1() -> solution.TreeNode:
    root = solution.TreeNode(val=3)
    
    root.left = solution.TreeNode(val=4)
    root.left.left = solution.TreeNode(val=5)
    root.left.right = solution.TreeNode(val=4)
    
    root.right = solution.TreeNode(val=5)
    root.right.right = solution.TreeNode(val=7)

    return root

def root_2a() -> solution.TreeNode:
    root = solution.TreeNode(val=1)
    return root

def root_2b() -> solution.TreeNode:
    root = solution.TreeNode(val=1)
    root.left = solution.TreeNode(val=2)
    return root

def expected_2() -> solution.TreeNode:
    root = solution.TreeNode(val=2)
    root.left = solution.TreeNode(val=2)
    return root

@pytest.mark.parametrize(
    "root1,root2,expected",
    [
        (root_1a(), root_1b(), expected_1()),
        (root_2a(), root_2b(), expected_2()),
    ],
)
def test_first_pass(root1, root2, expected):
    got = solution.first_pass(root1, root2)
    assert got.val == expected.val
