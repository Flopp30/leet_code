package main

import "fmt"

//Given the root of a binary tree, return its maximum depth.
//A binary tree's maximum depth is the number of nodes along the longest path
//from the root node down to the farthest leaf node.

//Example 1:
//Input: root = [3,9,20,null,null,15,7]
//Output: 3

//Example 2:
//Input: root = [1,null,2]
//Output: 2

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + max___(maxDepth(root.Left), maxDepth(root.Right))
}

func max___(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
func main() {
	tree := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:   2,
			Right: &TreeNode{Val: 3},
		},
	}
	fmt.Println(maxDepth(tree))
}
