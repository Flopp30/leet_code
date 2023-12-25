package main

import (
	"fmt"
	"sort"
)

//You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
//represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
//You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
//
//Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
//still does not have any overlapping intervals (merge overlapping intervals if necessary).
//
//Return intervals after the insertion.
//Example 1:
//
//Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
//Output: [[1,5],[6,9]]
//Example 2:
//
//Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
//Output: [[1,2],[3,10],[12,16]]
//Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
func insert(intervals [][]int, newInterval []int) [][]int {
	sortIntervals := func(intervals [][]int) {
		sort.Slice(intervals, func(i, j int) bool {
			return intervals[i][0] < intervals[j][0]
		})
	}
	intervals = append(intervals, newInterval)
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

func otherSolution(intervals [][]int, newInterval []int) [][]int {
	output := [][]int{}
	min := func(i, j int) int {
		if i < j {
			return i
		}
		return j
	}
	max := func(i, j int) int {
		if i > j {
			return i
		}
		return j
	}
	for i := 0; i < len(intervals); i++ {
		if newInterval[1] < intervals[i][0] {
			output = append(output, newInterval)
			return append(output, intervals[i:]...)
		} else if newInterval[0] > intervals[i][1] {
			output = append(output, intervals[i])
		} else {
			newInterval = []int{
				min(newInterval[0], intervals[i][0]),
				max(newInterval[1], intervals[i][1]),
			}
		}
	}

	output = append(output, newInterval)

	return output
}
func main() {
	fmt.Println(insert([][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, []int{4, 8}))
	fmt.Println(otherSolution([][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, []int{4, 8}))
}
