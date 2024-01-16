package main

import "fmt"

//Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
//
//In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

//Example 1:
//Input: rowIndex = 3
//Output: [1,3,3,1]

//Example 2:
//Input: rowIndex = 0
//Output: [1]

// Example 3:
// Input: rowIndex = 1
// Output: [1,1]
func getRow(rowIndex int) []int {
	res := []int{1}
	for k := 1; k <= rowIndex; k++ {
		nextVal := res[k-1] * (rowIndex - k + 1) / k
		res = append(res, nextVal)
	}
	return res
}

func main() {
	fmt.Println(getRow(5))
}
