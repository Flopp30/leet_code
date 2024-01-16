package main

import "fmt"

// Given an integer numRows, return the first numRows of Pascal's triangle.
//
// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
// Example 1:
//
// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// Example 2:
//
// Input: numRows = 1
// Output: [[1]]
func generate(numRows int) [][]int {
	var res [][]int
	if numRows == 0 {
		return res
	}
	res = append(res, []int{1})
	for i := 1; i < numRows; i++ {
		prevRow := res[i-1]
		newRow := []int{1}
		for j := 0; j < len(prevRow)-1; j++ {
			newRow = append(newRow, prevRow[j]+prevRow[j+1])
		}
		newRow = append(newRow, 1)
		res = append(res, newRow)
	}
	return res
}

func main() {
	fmt.Println(generate(5))
}
