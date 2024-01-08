package main

import (
	"fmt"
	"strconv"
)

// Given an integer n, return all the structurally unique BST's (binary search trees),
// which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
//
// Example 1:
// Input: n = 3
// Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
//
// Example 2:
// Input: n = 1
// Output: [[1]]

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees(n int) []*TreeNode {
	cache := make(map[string][]*TreeNode)
	return generate(1, n, cache)
}

func generate(start, end int, cache map[string][]*TreeNode) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}

	key := strconv.Itoa(start) + "-" + strconv.Itoa(end)
	if value, ok := cache[key]; ok {
		return value
	}

	var res []*TreeNode
	for i := start; i <= end; i++ {
		leftTrees := generate(start, i-1, cache)
		rightTrees := generate(i+1, end, cache)

		for _, l := range leftTrees {
			for _, r := range rightTrees {
				node := &TreeNode{Val: i}
				node.Left = l
				node.Right = r
				res = append(res, node)
			}
		}
	}

	cache[key] = res
	return res
}

func main() {
	fmt.Println(generateTrees(3))
}
