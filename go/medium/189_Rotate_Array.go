package main

import "fmt"

//Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
//
//Example 1:
//Input: nums = [1,2,3,4,5,6,7], k = 3
//Output: [5,6,7,1,2,3,4]
//Explanation:
//rotate 1 steps to the right: [7,1,2,3,4,5,6]
//rotate 2 steps to the right: [6,7,1,2,3,4,5]
//rotate 3 steps to the right: [5,6,7,1,2,3,4]
//
//Example 2:
//Input: nums = [-1,-100,3,99], k = 2
//Output: [3,99,-1,-100]
//Explanation:
//rotate 1 steps to the right: [99,-1,-100,3]
//rotate 2 steps to the right: [3,99,-1,-100]

func rotate(nums []int, k int) {
	if nums == nil {
		return
	}
	k %= len(nums)
	rotate_(nums, 0, len(nums)-1)
	rotate_(nums, 0, k-1)
	rotate_(nums, k, len(nums)-1)
}

func rotate_(nums []int, low, high int) {
	for low < high {
		nums[low], nums[high] = nums[high], nums[low]
		low++
		high--
	}
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(arr, 3)
	fmt.Println(arr)
}
