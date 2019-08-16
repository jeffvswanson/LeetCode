/*
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).package main

The binary search tree is guaranteed to have unique values.

Example 1:
	Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
	Output: 32

Example 2:
	Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
	Output: 23

Notes:
	1. The number of nodes in the tree is at most 10000.
	2. The final answer is guaranteed to be less than 2^31.
*/
package main

import "fmt"

// TreeNode is the element that composes a binary search tree.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, L int, R int) int {

	if root == nil {
		return 0
	} else if root.Val > R {
		// Go left because all right children of R will be greater than R by definition of a BST.
		return rangeSumBST(root.Left, L, R)
	} else if root.Val < L {
		// Go right because all left children of L will be less than L by definition of a BST.
		return rangeSumBST(root.Right, L, R)
	}
	return root.Val + rangeSumBST(root.Right, L, R) + rangeSumBST(root.Left, L, R)
}

func main() {
	fmt.Println("Hello!")
}
