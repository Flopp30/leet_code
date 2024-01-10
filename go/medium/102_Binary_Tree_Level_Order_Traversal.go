package main

import "fmt"

//Given the root of a binary tree, return the level order traversal
//of its nodes' values. (i.e., from left to right, level by level).

//Example 1:
//Input: root = [3,9,20,null,null,15,7]
//Output: [[3],[9,20],[15,7]]

//Example 2:
//Input: root = [1]
//Output: [[1]]

//Example 3:
//Input: root = []
//Output: []

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func levelOrder(root *TreeNode) [][]int {
	var result [][]int

	customLevelOrder(root, &result, 0)

	return result
}

func customLevelOrder(root *TreeNode, preResult *[][]int, level int) {
	if root == nil {
		return
	}

	if len(*preResult) == level {
		*preResult = append(*preResult, []int{})
	}

	(*preResult)[level] = append((*preResult)[level], root.Val)

	customLevelOrder(root.Left, preResult, level+1)
	customLevelOrder(root.Right, preResult, level+1)
}

func main() {
	tree := &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val: 9,
		},
		Right: &TreeNode{
			Val: 20,
			Left: &TreeNode{
				Val: 15,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
	}
	fmt.Println(levelOrder(tree))
}
