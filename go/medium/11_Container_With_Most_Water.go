package main

import "fmt"

// You are given an integer array height of length n.
// There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// Find two lines that together with the x-axis form a container,
// such that the container contains the most water.
// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.
//
// Example 1:
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
//
// Example 2:
// Input: height = [1,1]
// Output: 1
func maxArea(height []int) int {
	calculateArea := func(low, high, first, second int) int {
		if second > first {
			return first * (high - low)
		}
		return second * (high - low)
	}
	leftPointer, rightPointer := 0, len(height)-1
	maxSum := 0
	for leftPointer < rightPointer {
		newSum := calculateArea(leftPointer, rightPointer, height[leftPointer], height[rightPointer])
		if newSum > maxSum {
			maxSum = newSum
		}
		if height[leftPointer] < height[rightPointer] {
			leftPointer++
		} else {
			rightPointer--
		}
	}
	return maxSum
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
