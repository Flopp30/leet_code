package main

import (
	"fmt"
)

//Given a triangle array, return the minimum path sum from top to bottom.
//
//For each step, you may move to an adjacent number of the row below. More formally,
//if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
//
//Example 1:
//Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
//Output: 11
//Explanation: The triangle looks like:
//2
//3 4
//6 5 7
//4 1 8 3
//The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

//Example 2:
//Input: triangle = [[-10]]
//Output: -10

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	for i := 1; i < n; i++ {
		for j := 0; j <= i; j++ {
			switch j {
			case 0:
				triangle[i][j] += triangle[i-1][j]
			case i:
				triangle[i][j] += triangle[i-1][j-1]
			default:
				triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
			}
		}
	}

	res := triangle[n-1][0]
	for i := 1; i < n; i++ {
		res = min(res, triangle[n-1][i])
	}
	return res
}
func main() {
	triangle := [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}
	fmt.Println(minimumTotal(triangle))
}
