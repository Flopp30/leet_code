package main

import "fmt"

//Given the root of a binary tree, return the postorder traversal of its nodes' values.
//
//Example 1:
//Input: root = [1,null,2,3]
//Output: [3,2,1]
//
//Example 2:
//Input: root = []
//Output: []
//
//Example 3:
//Input: root = [1]
//Output: [1]

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func postorderHelper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}
	postorderHelper(root.Left, res)
	postorderHelper(root.Right, res)
	*res = append(*res, root.Val)
}

func postorderTraversal(root *TreeNode) []int {
	var res []int
	postorderHelper(root, &res)
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
	fmt.Println(postorderTraversal(tree))
}
