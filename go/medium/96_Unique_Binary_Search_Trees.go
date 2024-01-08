package main

import (
	"strconv"
)

// Given an integer n, return the number of structurally unique BST's (binary search trees)
// which has exactly n nodes of unique values from 1 to n.
//
// Example 1:
// Input: n = 3
// Output: 5
//
// Example 2:
// Input: n = 1
// Output: 1
func numTrees(n int) int {
	cache := make(map[string]int)
	return generate_(n, cache)
}

func generate_(n int, cache map[string]int) int {
	if n == 0 || n == 1 {
		return 1
	}

	key := strconv.Itoa(n) + "-"
	if value, ok := cache[key]; ok {
		return value
	}

	var l, r, res int
	for root := 1; root <= n; root++ {
		l = generate_(root-1, cache)
		r = generate_(n-root, cache)
		res += l * r
	}

	cache[key] = res
	return res
}
