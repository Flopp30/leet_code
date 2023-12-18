package main

import (
	"fmt"
)

//Given an integer x, return true if x is a
//palindrome
//, and false otherwise.
//
//Input: x = 121
//Output: true
//Explanation: 121 reads as 121 from left to right and from right to left.\
//
//Input: x = -121
//Output: false
//Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
//Therefore it is not a palindrome.

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	reversed := 0
	original := x
	for original != 0 {
		digit := original % 10
		reversed = reversed*10 + digit
		original /= 10
	}
	return reversed == x
}

func main() {
	fmt.Println(isPalindrome(100))
	fmt.Println(isPalindrome(1001))
}
