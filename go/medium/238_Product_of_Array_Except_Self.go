package main

import "fmt"

// Given an integer array nums, return an array answer such that answer[i] is equal to the product
// of all the elements of nums except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.
//
// Example 1:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
//
// Example 2:
// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]
func productExceptSelf(nums []int) []int {
	size := len(nums)
	res := make([]int, size)
	res[0], res[size-1] = 1, 1
	for i := 1; i < size; i++ {
		res[i] = res[i-1] * nums[i-1]
	}
	right := 1
	for i := size - 2; i >= 0; i-- {
		right *= nums[i+1]
		res[i] *= right
	}
	return res
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{-1, 1, 0, -3, 3}))
}
