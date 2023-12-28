package main

import "fmt"

// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
//
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.Given an m x n grid of characters board and a string word, return true if word exists in the grid.
//
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
//
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true
//
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
// Output: true
//
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
// Output: false

func exist(board [][]byte, word string) bool {
	found := false
	m, n := len(board), len(board[0])
	var dfs func(i, j, k int)
	dfs = func(i, j, k int) {
		if i < 0 || j < 0 || i >= m || j >= n {
			return
		}
		if board[i][j] == '*' {
			return
		}
		if board[i][j] != word[k] {
			return
		}
		if k == len(word)-1 {
			found = true
			return
		}
		tmp := board[i][j]
		board[i][j] = '*'

		dfs(i-1, j, k+1)
		dfs(i+1, j, k+1)
		dfs(i, j-1, k+1)
		dfs(i, j+1, k+1)

		board[i][j] = tmp
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			k := 0
			dfs(i, j, k)
		}
	}
	return found
}

func main() {
	//fmt.Println(exist([][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "ABCCED"))
	fmt.Println(exist([][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "SEE"))
	//fmt.Println(exist([][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "ABCB"))
}
