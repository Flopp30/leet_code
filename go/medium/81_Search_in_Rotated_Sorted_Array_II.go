package main

import "fmt"

//There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
//Before being passed to your function, nums is rotated at an unknown pivot
//index k (0 <= k < nums.length) such that the resulting
//array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
//For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
//Given the array nums after the rotation and an integer target,
//return true if target is in nums, or false if it is not in nums.
//You must decrease the overall operation steps as much as possible.

//Example 1:
//Input: nums = [2,5,6,0,0,1,2], target = 0
//Output: true

// Example 2:
// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false
func search_(nums []int, target int) bool {
	low, high := 0, len(nums)-1
	for low <= high {
		for low < high && nums[low] == nums[low+1] {
			low++
		}
		for high > low && nums[high] == nums[high-1] {
			high--
		}
		mid := (low + high) / 2
		if nums[mid] == target {
			return true
		}
		if nums[low] <= nums[mid] {
			if nums[low] <= target && target <= nums[mid] {
				high = mid - 1
			} else {
				low = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
	}
	return false
}

func main() {
	fmt.Println(search_([]int{4, 5, 6, 7, 0, 1, 2}, 0))
}
