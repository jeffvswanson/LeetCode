"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Examples
--------
Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints
-----------
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        tree = []
        tree.extend(self.inorderTraversal(root.left))
        tree.append(root.val)
        tree.extend(self.inorderTraversal(root.right))

        return tree