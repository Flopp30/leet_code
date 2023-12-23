package main

import "fmt"

//Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
//Example 1:
//
//Input: n = 3
//Output: [[1,2,3],[8,9,4],[7,6,5]]
//Example 2:
//
//Input: n = 1
//Output: [[1]]
func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
		for j := 0; j < n; j++ {
			matrix[i][j] = 0
		}
	}
	direction := "right"
	directionsCount := 1
	i, j := 0, 0
	for k := 1; k <= n*n; k++ {
		matrix[i][j] = k
		switch direction {
		case "right":
			if j != n-1-directionsCount/4 {
				j++
			} else {
				direction = "down"
				directionsCount++
				i++
			}
			continue
		case "down":
			if i != n-1-directionsCount/4 {
				i++
			} else {
				direction = "left"
				directionsCount++
				j--
			}
		case "left":
			if j != directionsCount/4 {
				j--
			} else {
				direction = "up"
				directionsCount++
				i--
			}
		case "up":
			if i != directionsCount/4 {
				i--
			} else {
				direction = "right"
				directionsCount++
				j++
			}
		}
	}
	return matrix
}

func generateMatrix2(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}

	num := 1
	top, bottom, left, right := 0, n-1, 0, n-1

	for num <= n*n {
		for i := left; i <= right; i++ {
			matrix[top][i] = num
			num++
		}
		top++

		for i := top; i <= bottom; i++ {
			matrix[i][right] = num
			num++
		}
		right--

		for i := right; i >= left; i-- {
			matrix[bottom][i] = num
			num++
		}
		bottom--

		for i := bottom; i >= top; i-- {
			matrix[i][left] = num
			num++
		}
		left++
	}

	return matrix
}

func main() {
	fmt.Println(generateMatrix(3))
	fmt.Println(generateMatrix(5))
	fmt.Println(generateMatrix2(5))
}
