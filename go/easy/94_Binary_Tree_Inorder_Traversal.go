package main

import "fmt"

// Given the root of a binary tree, return the inorder traversal of its nodes' values.
//
// Example 1:
// Input: root = [1,null,2,3]
// Output: [1,3,2]
//
// Example 2:
// Input: root = []
// Output: []
//
// Example 3:
// Input: root = [1]
// Output: [1]

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func helper(root *TreeNode, res []int) []int {
	if root == nil {
		return res
	}
	res = helper(root.Left, res)
	res = append(res, root.Val)
	res = helper(root.Right, res)
	return res
}

func inorderTraversal(root *TreeNode) []int {
	return helper(root, []int{})
}

func inorderTraversalStack(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	curr := root

	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}

		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, curr.Val)

		curr = curr.Right
	}

	return res
}

func main() {
	tree := &TreeNode{
		Val:  1,
		Left: nil,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:   3,
				Left:  nil,
				Right: nil,
			},
			Right: nil,
		},
	}
	fmt.Println(inorderTraversal(tree))
	fmt.Println(inorderTraversalStack(tree))
}
