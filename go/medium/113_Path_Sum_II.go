package main

import "fmt"

//Given the root of a binary tree and an integer targetSum,
//return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
//Each path should be returned as a list of the node values, not node references.
//
//A root-to-leaf path is a path starting from the root and ending at any leaf node.
//A leaf is a node with no children.
//
//Example 1:
//Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
//Output: [[5,4,11,2],[5,8,4,5]]
//Explanation: There are two paths whose sum equals targetSum:
//5 + 4 + 11 + 2 = 22
//5 + 8 + 4 + 5 = 22
//
//Example 2:
//Input: root = [1,2,3], targetSum = 5
//Output: []
//
//Example 3:
//Input: root = [1,2], targetSum = 0
//Output: []

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func pathSumHelper(root *TreeNode, currentSum, targetSum int, path []int, res *[][]int) {
	if root == nil {
		return
	}
	path = append(path, root.Val)
	if root.Left == nil && root.Right == nil {
		if targetSum == currentSum+root.Val {
			*res = append(*res, append([]int{}, path...))
		}
		return
	}

	pathSumHelper(root.Left, currentSum+root.Val, targetSum, path, res)
	pathSumHelper(root.Right, currentSum+root.Val, targetSum, path, res)
	path = path[:len(path)-1]
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	path := make([]int, 0)
	res := make([][]int, 0)
	pathSumHelper(root, 0, targetSum, path, &res)
	return res
}

func main() {
	tree := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 4,
			},
		},
	}
	fmt.Println(pathSum(tree, 8))
}
