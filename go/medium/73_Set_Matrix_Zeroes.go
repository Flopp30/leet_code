package main

import (
	"fmt"
)

// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
//
// You must do it in place.
//
// Example 1:
// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]
//
// Example 2:
// Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
// Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

// [1,1,1],
// [1,0,1],
// [1,1,1]
// 1 2 3  target = 9
// 4 5 6
// 7 8 9
func setZeroes(matrix [][]int) {
	m := len(matrix)
	n := len(matrix[0])
	var columns []int
	var rows []int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				columns = append(columns, j)
				rows = append(rows, i)
			}
		}
	}
	for _, row := range rows {
		for j := 0; j < n; j++ {
			matrix[row][j] = 0
		}
	}
	for _, column := range columns {
		for i := 0; i < m; i++ {
			matrix[i][column] = 0
		}
	}
}

func main() {
	matrix := [][]int{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}
	setZeroes(matrix)
	fmt.Println(matrix)
	matrix = [][]int{{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}}
	setZeroes(matrix)
	fmt.Println(matrix)
}
