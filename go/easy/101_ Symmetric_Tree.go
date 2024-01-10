package main

import "fmt"

//Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
//
//	Example 1:
//Input: root = [1,2,2,3,4,4,3]
//Output: true
//
//Example 2:
//Input: root = [1,2,2,null,3,null,3]
//Output: false

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func isSymmetricHelper(left, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil || left.Val != right.Val {
		return false
	}
	return isSymmetricHelper(left.Left, right.Right) && isSymmetricHelper(left.Right, right.Left)
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return isSymmetricHelper(root.Left, root.Right)
}

func main() {
	tree := &TreeNode{
		1,
		&TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
		&TreeNode{
			Val: 2,
			Right: &TreeNode{
				Val: 3,
			},
		},
	}
	fmt.Println(isSymmetric(tree))
}
