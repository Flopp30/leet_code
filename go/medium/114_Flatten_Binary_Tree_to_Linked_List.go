package main

import "fmt"

//Given the root of a binary tree, flatten the tree into a "linked list":
//
//The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
//The "linked list" should be in the same order as a pre-order traversal of the binary tree.
//
//
//Example 1:
//Input: root = [1,2,5,3,4,null,6]
//Output: [1,null,2,null,3,null,4,null,5,null,6]
//
//Example 2:
//Input: root = []
//Output: []
//
//Example 3:
//Input: root = [0]
//Output: [0]

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func flattenHelper(root *TreeNode) *TreeNode {
	pre := &TreeNode{}
	for root != nil {
		if root.Left != nil {
			tmp := flattenHelper(root.Left)
			tmp.Right = root.Right

			root.Right = root.Left
			root.Left = nil
		}

		pre = root
		root = root.Right
	}
	return pre
}
func flatten(root *TreeNode) {
	flattenHelper(root)
}

func main() {
	tree := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
			Right: &TreeNode{
				Val: 4,
			},
		},
		Right: &TreeNode{
			Val: 5,
			Right: &TreeNode{
				Val: 6,
			},
		},
	}
	flatten(tree)
	for tree != nil {
		fmt.Println(tree.Val)
		tree = tree.Right
	}
}
