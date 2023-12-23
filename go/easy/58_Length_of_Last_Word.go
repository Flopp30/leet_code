package main

import (
	"fmt"
)

//Given a string s consisting of words and spaces, return the length of the last word in the string.
//A word is a maximal
//substring
//consisting of non-space characters only.
//Example 1:
//
//Input: s = "Hello World"
//Output: 5
//Explanation: The last word is "World" with length 5.
//Example 2:
//
//Input: s = "   fly me   to   the moon  "
//Output: 4
//Explanation: The last word is "moon" with length 4.
//Example 3:
//
//Input: s = "luffy is still joyboy"
//Output: 6
//Explanation: The last word is "joyboy" with length 6.

//func lengthOfLastWord(s string) int {
//	words := strings.Split(strings.TrimSpace(s), " ")
//	return len(words[len(words)-1])
//}

func lengthOfLastWord(s string) int {
	length := 0
	for i := len(s) - 1; i >= 0; i-- {
		if string(s[i]) == " " {
			if length == 0 {
				continue
			} else {
				return length
			}
		}
		length++
	}
	return length
}

func main() {
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
}
