package main

import "fmt"

//Given the root of a binary tree, return the preorder traversal of its nodes' values.

//Example 1:
//Input: root = [1,null,2,3]
//Output: [1,2,3]

//Example 2:
//Input: root = []
//Output: []

//Example 3:
//Input: root = [1]
//Output: [1]

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func preorderHelper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}
	*res = append(*res, root.Val)
	preorderHelper(root.Left, res)
	preorderHelper(root.Right, res)
}

func preorderTraversal(root *TreeNode) []int {
	var res []int
	preorderHelper(root, &res)
	return res
}

func main() {
	tree := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 0,
		},
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
	}
	fmt.Println(preorderTraversal(tree))
}
