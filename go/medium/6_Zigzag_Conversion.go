package main

import (
	"fmt"
	"strings"
)

// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
//
// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"
//
// Write the code that will take a string and make this conversion given a number of rows:
//
// string convert(string s, int numRows);
//
// Example 1:
// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
//
//	P   A   H   N
//	A P L S I I G
//	Y   I   R
//
// Example 2:
// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
//
// Example 3:
// Input: s = "A", numRows = 1
// Output: "A"
// directions: down i + 1; const j
// up i - 1; j + 1
func convert(s string, numRows int) string {
	if numRows == 1 || numRows == 0 {
		return s
	}
	resMap := make([][]string, numRows)
	cycleLen := numRows*2 - 2
	for i, ch := range s {
		pos := i % cycleLen
		if pos < numRows {
			resMap[pos] = append(resMap[pos], string(ch))
		} else {
			resMap[cycleLen-pos] = append(resMap[cycleLen-pos], string(ch))
		}
	}
	var res strings.Builder
	for _, row := range resMap {
		res.WriteString(strings.Join(row, ""))
	}
	return res.String()
}
func main() {
	fmt.Println(convert("PAYPALISHIRING", 3))
	fmt.Println(convert("PAYPALISHIRING", 4))
	fmt.Println(convert("A", 1))
}
