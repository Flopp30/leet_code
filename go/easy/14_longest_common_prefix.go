package main

import (
	"fmt"
	"strings"
)

//
//Write a function to find the longest common prefix string amongst an array of strings.
//
//If there is no common prefix, return an empty string "".
//
//Example 1:
//
//Input: strs = ["flower","flow","flight"]
//Output: "fl"
//Example 2:
//
//Input: strs = ["dog","racecar","car"]
//Output: ""
//Explanation: There is no common prefix among the input strings.

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	var res strings.Builder
	minLen := len(strs[0])

	for _, str := range strs {
		if len(str) < minLen {
			minLen = len(str)
		}
	}

	for i := 0; i < minLen; i++ {
		curEl := strs[0][i : i+1]

		for _, str := range strs {
			if str[i:i+1] != curEl {
				return res.String()
			}
		}

		res.WriteString(curEl)
	}

	return res.String()
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"dog", "racecar", "car"}))
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
}
