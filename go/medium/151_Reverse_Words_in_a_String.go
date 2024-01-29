package main

import (
	"fmt"
	"strings"
)

// Given an input string s, reverse the order of the words.
//
// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
//
// Return a string of the words in reverse order concatenated by a single space.
//
// Note that s may contain leading or trailing spaces or multiple spaces between two words.
// The returned string should only have a single space separating the words. Do not include any extra spaces.
//
// Example 1:
//
// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Example 2:
//
// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:
//
// Input: s = "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

func reverseWords(s string) string {
	words := strings.Fields(s)

	low, high := 0, len(words)-1

	for low < high {
		words[low], words[high] = words[high], words[low]
		low++
		high--
	}

	return strings.TrimSpace(strings.Join(words, " "))
}
func main() {
	fmt.Println(reverseWords("the sky is blue"))
	fmt.Println(reverseWords("a good   example"))
	fmt.Println(reverseWords("  hello world  "))
}
