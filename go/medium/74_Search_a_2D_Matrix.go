package main

import "fmt"

// You are given an m x n integer matrix with the following two properties:
//
// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.
//
// You must write a solution in O(log(m * n)) time complexity.
//
// Example 1:
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true
//
// Example 2:
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false
func searchMatrix(matrix [][]int, target int) bool {
	height := len(matrix)
	width := len(matrix[0])
	targetRow := -1
	for row := 0; row < height; row++ {
		if matrix[row][width-1] >= target {
			targetRow = row
			break
		}

	}
	if targetRow < 0 {
		return false
	}
	row := matrix[targetRow]
	width = len(row) - 1
	for width >= 0 {
		if row[width] > target {
			row = row[:width]
		} else if row[width] < target {
			row = row[width+1:]
		} else {
			return true
		}
		width = len(row) - 1
	}
	return false
}

func main() {
	fmt.Println(searchMatrix([][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 3))
	fmt.Println(searchMatrix([][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 13))
	fmt.Println(searchMatrix([][]int{{1, 3}}, 1))
}
