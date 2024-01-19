package main

import "fmt"

//You are given the root of a binary tree containing digits from 0 to 9 only.
//
//Each root-to-leaf path in the tree represents a number.
//
//For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
//Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
//
//A leaf node is a node with no children.
//
//
//Example 1:
//Input: root = [1,2,3]
//Output: 25
//Explanation:
//The root-to-leaf path 1->2 represents the number 12.
//The root-to-leaf path 1->3 represents the number 13.
//Therefore, sum = 12 + 13 = 25.
//
//Example 2:
//Input: root = [4,9,0,5,1]
//Output: 1026
//Explanation:
//The root-to-leaf path 4->9->5 represents the number 495.
//The root-to-leaf path 4->9->1 represents the number 491.
//The root-to-leaf path 4->0 represents the number 40.
//Therefore, sum = 495 + 491 + 40 = 1026.

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func sumNumbersHelper(root *TreeNode, currentSum int) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return currentSum*10 + root.Val
	}
	return sumNumbersHelper(root.Left, currentSum*10+root.Val) + sumNumbersHelper(root.Right, currentSum*10+root.Val)
}

func sumNumbers(root *TreeNode) int {
	return sumNumbersHelper(root, 0)
}

func main() {
	tree1 := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
		Right: &TreeNode{
			Val: 3,
		},
	}
	tree2 := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 9,
			Left: &TreeNode{
				Val: 5,
			},
			Right: &TreeNode{
				Val: 1,
			},
		},
		Right: &TreeNode{
			Val: 0,
		},
	}
	fmt.Println(sumNumbers(tree1))
	fmt.Println(sumNumbers(tree2))
}
