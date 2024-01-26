package main

import "fmt"

//Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
//
//A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
//of the characters without disturbing the relative positions of the remaining characters.
//(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
//
//Example 1:
//Input: s = "abc", t = "ahbgdc"
//Output: true
//
//Example 2:
//Input: s = "axc", t = "ahbgdc"
//Output: false

func isSubsequence(s string, t string) bool {
	if s == "" {
		return true
	}
	pointer, walker := 0, 0
	for walker < len(t) {
		if s[pointer] == t[walker] {
			pointer++
		}
		if pointer == len(s) {
			return true
		}
		walker++
	}
	return pointer == len(s)
}

func main() {
	fmt.Println(isSubsequence("abc", "ahbgdc"))
	fmt.Println(isSubsequence("axc", "ahbgdc"))
}
