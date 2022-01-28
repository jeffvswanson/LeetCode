"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Examples
--------
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints
-----------
* The number of nodes in the tree is in the range [0, 104].
* -100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)

    def bfs_traversal(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)

        # pre-processing work
        levels = 0
        unvisited_nodes_on_level = 1

        while q:
            root = q.popleft()
            unvisited_nodes_on_level -= 1
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if unvisited_nodes_on_level == 0:
                levels += 1
                unvisited_nodes_on_level = len(q)

        return levels
