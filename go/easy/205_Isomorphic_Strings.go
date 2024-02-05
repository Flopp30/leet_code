package main

import "fmt"

// Given two strings s and t, determine if they are isomorphic.
//
// Two strings s and t are isomorphic if the characters in s can be replaced to get t.
//
// All occurrences of a character must be replaced with another character while preserving the order of characters.
// No two characters may map to the same character, but a character may map to itself.
//
// Example 1:
// Input: s = "egg", t = "add"
// Output: true
//
// Example 2:
// Input: s = "foo", t = "bar"
// Output: false
//
// Example 3:
// Input: s = "paper", t = "title"
// Output: true
func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	hashmapS, hashmapT := make(map[string]string), make(map[string]string)
	for i := 0; i < len(s); i++ {
		elS := string(s[i])
		elT := string(t[i])
		if val, ok := hashmapS[elS]; ok {
			if val != elT {
				return false
			}
		} else {
			if _, ok := hashmapT[elT]; ok {
				return false
			}
			hashmapS[elS] = elT
			hashmapT[elT] = elS
		}
	}
	return true
}

func main() {
	fmt.Println(isIsomorphic("egg", "add"))
	fmt.Println(isIsomorphic("foo", "bar"))
	fmt.Println(isIsomorphic("paper", "title"))
}
