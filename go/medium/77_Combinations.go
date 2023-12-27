package main

import "fmt"

// Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
//
// You may return the answer in any order.
// Example 1:
//
// Input: n = 4, k = 2
// Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
// Explanation: There are 4 choose 2 = 6 total combinations.
// Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
// Example 2:
//
// Input: n = 1, k = 1
// Output: [[1]]
// Explanation: There is 1 choose 1 = 1 total combination.
func combine(n int, k int) [][]int {
	var res [][]int
	dfs(&res, nil, 1, n, k)
	return res
}

func dfs(res *[][]int, path []int, start, n, k int) {
	if len(path) == k {
		*res = append(*res, path)
		return
	}
	for i := start; i <= n; i++ {
		temp := append([]int{}, path...)
		dfs(res, append(temp, i), i+1, n, k)
	}
}

func main() {
	fmt.Println(combine(4, 2))
}
