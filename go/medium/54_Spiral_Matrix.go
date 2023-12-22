package main

//Given an m x n matrix, return all elements of the matrix in spiral order.
//
//Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
//Output: [1,2,3,6,9,8,7,4,5]
//
//Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
//Output: [1,2,3,4,8,12,11,10,9,5,6,7]
import "fmt"

func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	res := make([]int, m*n)

	i, j, k := 0, 0, 0
	direction := "Right"
	for k < m*n {
		res[k] = matrix[i][j]
		switch direction {
		case "Right":
			if i+j == n-1 {
				direction = "Down"
				i++
			} else {
				j++
			}
		case "Down":
			if n-j == m-i {
				direction = "Left"
				j--
			} else {
				i++
			}
		case "Left":
			if i+j == m-1 {
				direction = "Up"
				i--
			} else {
				j--
			}
		case "Up":
			if i-j == 1 {
				direction = "Right"
				j++
			} else {
				i--
			}
		}
		k++
	}
	return res
}
func main() {
	fmt.Println(spiralOrder([][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}))
	fmt.Println(spiralOrder([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
}
