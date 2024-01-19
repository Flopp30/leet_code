package main

import "fmt"

//Given an integer array nums where every element appears three times except for one,
//which appears exactly once. Find the single element and return it.
//
//You must implement a solution with a linear runtime complexity and use only constant extra space.
//
//Example 1:
//Input: nums = [2,2,3,2]
//Output: 3
//
//Example 2:
//Input: nums = [0,1,0,1,0,1,99]
//Output: 99

func singleNumber(nums []int) int {
	ones := 0
	twos := 0

	for _, n := range nums {
		ones ^= n & ^twos
		twos ^= n & ^ones
	}
	return ones
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 3, 2}))
	fmt.Println(singleNumber([]int{0, 1, 0, 1, 0, 1, 99}))
}
