package main

//Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
//determine if the input string is valid.
//An input string is valid if:
//Open brackets must be closed by the same type of brackets.
//Open brackets must be closed in the correct order.
//Every close bracket has a corresponding open bracket of the same type.
//
//
//Example 1:
//
//Input: s = "()"
//Output: true
//Example 2:
//
//Input: s = "()[]{}"
//Output: true
//Example 3:
//
//Input: s = "(]"
//Output: false

import "fmt"

func isValid(s string) bool {
	if len(s)%2 != 0 || len(s) == 0 {
		return false
	}
	bracketMap := map[rune]rune{
		']': '[',
		'}': '{',
		')': '(',
	}

	stack := []rune{}
	for _, bracket := range s {
		if openBracket, ok := bracketMap[bracket]; ok {
			if len(stack) == 0 || stack[len(stack)-1] != openBracket {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, bracket)
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("){"))
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}
