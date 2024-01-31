package main

import "fmt"

//Given two strings ransomNote and magazine, return true if ransomNote can be constructed
//by using the letters from magazine and false otherwise.
//Each letter in magazine can only be used once in ransomNote.

//Example 1:
//Input: ransomNote = "a", magazine = "b"
//Output: false

//Example 2:
//Input: ransomNote = "aa", magazine = "ab"
//Output: false

// Example 3:
// Input: ransomNote = "aa", magazine = "aab"
// Output: true
func canConstruct(ransomNote string, magazine string) bool {
	if len(ransomNote) > len(magazine) {
		return false
	}
	hashmap := make(map[rune]int)
	for _, r := range magazine {
		hashmap[r]++
	}
	for _, r := range ransomNote {
		if _, ok := hashmap[r]; ok {
			hashmap[r]--
			if hashmap[r] == 0 {
				delete(hashmap, r)
			}
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(canConstruct("a", "b"))
	fmt.Println(canConstruct("aa", "ab"))
	fmt.Println(canConstruct("aa", "aab"))
}
