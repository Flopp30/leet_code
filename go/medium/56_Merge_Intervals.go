package main

import (
	"fmt"
	"sort"
)

//Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
//and return an array of the non-overlapping intervals that cover all the intervals in the input.
//
//Example 1:
//
//Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
//Output: [[1,6],[8,10],[15,18]]
//Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
//Example 2:
//
//Input: intervals = [[1,4],[4,5]]
//Output: [[1,5]]
//Explanation: Intervals [1,4] and [4,5] are considered overlapping.
func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {

		return intervals
	}
	sortIntervals := func(intervals [][]int) {
		sort.Slice(intervals, func(i, j int) bool {

			return intervals[i][0] < intervals[j][0]
		})
	}

	sortIntervals(intervals)

	mergedIntervals := make([][]int, 0, len(intervals))
	mergedIntervals = append(mergedIntervals, intervals[0])

	for _, interval := range intervals[1:] {
		if top := mergedIntervals[len(mergedIntervals)-1]; interval[0] > top[1] {
			mergedIntervals = append(mergedIntervals, interval)
		} else if interval[1] > top[1] {
			top[1] = interval[1]
		}
	}

	return mergedIntervals
}

func main() {
	fmt.Println(merge([][]int{{1, 3}, {2, 6}, {8, 10}}))
	fmt.Println(merge([][]int{{1, 4}, {4, 6}}))
}
