package main

import (
	"fmt"
)

//https://leetcode.com/problems/longest-substring-without-repeating-characters/
//Given a string s, find the length of the longest substring without repeating characters.
//Example 1:
//
//Input: s = "abcabcbb"
//Output: 3
//Explanation: The answer is "abc", with the length of 3.

func lengthOfLongestSubstring(s string) int {
	hashmap := make(map[uint8]int)
	var leftPointer, rightPointer, result int
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for rightPointer < len(s) {
		var rightChar = s[rightPointer]
		hashmap[rightChar] += 1
		for hashmap[rightChar] > 1 {
			leftChar := s[leftPointer]
			hashmap[leftChar] -= 1
			leftPointer += 1
		}
		result = max(result, rightPointer-leftPointer+1)

		rightPointer += 1
	}
	return result
}

func main() {
	fmt.Println(lengthOfLongestSubstring("aaa"))
	fmt.Println(lengthOfLongestSubstring("abcabaa"))
}
