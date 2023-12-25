package main

import "fmt"

//Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
//
//You have the following three operations permitted on a word:
//
//Insert a character
//Delete a character
//Replace a character
//
//
//Example 1:
//
//Input: word1 = "horse", word2 = "ros"
//Output: 3
//Explanation:
//horse -> rorse (replace 'h' with 'r')
//rorse -> rose (remove 'r')
//rose -> ros (remove 'e')
//Example 2:
//
//Input: word1 = "intention", word2 = "execution"
//Output: 5
//Explanation:
//intention -> inention (remove 't')
//inention -> enention (replace 'i' with 'e')
//enention -> exention (replace 'n' with 'x')
//exention -> exection (replace 'n' with 'c')
//exection -> execution (insert 'u')
func minDistance(word1 string, word2 string) int {
	pre := make([]int, len(word2)+1)
	cur := make([]int, len(word2)+1)
	min := func(nums ...int) int {
		ans := nums[0]
		for _, v := range nums {
			if v < ans {
				ans = v
			}
		}
		return ans
	}
	for i := 0; i < len(pre); i++ {
		pre[i] = i
	}
	for i := 1; i <= len(word1); i++ {
		cur[0] = i
		for j := 1; j < len(pre); j++ {
			if word1[i-1] != word2[j-1] {
				cur[j] = min(cur[j-1], pre[j-1], pre[j]) + 1
			} else {
				cur[j] = pre[j-1]
			}
		}
		tmp := make([]int, len(cur))
		copy(tmp, cur)
		pre = tmp
	}
	return pre[len(word2)]
}

func main() {
	fmt.Println(minDistance("horse", "ros"))
	fmt.Println(minDistance("intention", "execution"))
}
