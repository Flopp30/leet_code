package main

//Given a binary tree, determine if it is
//height-balanced
//
//Example 1:
//Input: root = [3,9,20,null,null,15,7]
//Output: true
//
//Example 2:
//Input: root = [1,2,2,3,3,null,null,4,4]
//Output: false
//
//Example 3:
//Input: root = []
//Output: true

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	dif := maxDepth_(root.Left) - maxDepth_(root.Right)
	if dif <= 1 && dif >= -1 {
		return isBalanced(root.Left) && isBalanced(root.Right)
	}
	return false
}

func maxDepth_(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + max_(maxDepth_(root.Left), maxDepth_(root.Right))
}

func max_(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
