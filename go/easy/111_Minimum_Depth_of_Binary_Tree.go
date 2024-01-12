package main

import "fmt"

//Given a binary tree, find its minimum depth.
//The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
//Note: A leaf is a node with no children.
//
//Example 1:
//Input: root = [3,9,20,null,null,15,7]
//Output: 2

//Example 2:
//Input: root = [2,null,3,null,4,null,5,null,6]
//Output: 5

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + min_(minDepth(root.Left), minDepth(root.Right))
}

func min_(a, b int) int {
	if a == 0 {
		return b
	}
	if b == 0 {
		return a
	}
	if a > b {
		return b
	}
	return a
}
func main() {
	tree := &TreeNode{
		Val:  1,
		Left: &TreeNode{Val: 2},
		Right: &TreeNode{
			Val: 2,
			Right: &TreeNode{
				Val: 3,
				Right: &TreeNode{
					Val: 4,
				},
			},
		},
	}
	fmt.Println(minDepth(tree))
}
