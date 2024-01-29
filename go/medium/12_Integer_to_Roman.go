package main

import (
	"fmt"
	"strings"
)

//Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
//
//Symbol       Value
//I             1
//V             5
//X             10
//L             50
//C             100
//D             500
//M             1000
//For example, 2 is written as II in Roman numeral, just two one's added together.
//12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
//
//Roman numerals are usually written largest to smallest from left to right.
//However, the numeral for four is not IIII. Instead, the number four is written as IV.
//Because the one is before the five we subtract it making four. The same principle applies to the number nine,
//which is written as IX. There are six instances where subtraction is used:
//
//I can be placed before V (5) and X (10) to make 4 and 9.
//X can be placed before L (50) and C (100) to make 40 and 90.
//C can be placed before D (500) and M (1000) to make 400 and 900.
//Given an integer, convert it to a roman numeral.

//Example 1:
//Input: num = 3
//Output: "III"
//Explanation: 3 is represented as 3 ones.
//
//Example 2:
//Input: num = 58
//Output: "LVIII"
//Explanation: L = 50, V = 5, III = 3.
//
//Example 3:
//Input: num = 1994
//Output: "MCMXCIV"
//Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

var letterMap = map[int]string{
	1:    "I",
	5:    "V",
	10:   "X",
	50:   "L",
	100:  "C",
	500:  "D",
	1000: "M",
	4:    "IV",
	9:    "IX",
	40:   "XL",
	90:   "XC",
	400:  "CD",
	900:  "CM",
}
var allowedKeys = []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

func intToRoman(num int) string {
	res := ""
	for _, key := range allowedKeys {
		if key > num {
			continue
		}
		for num >= key {
			res += letterMap[key]
			num -= key
		}
	}
	return res
}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	var res strings.Builder
	minLength := len(strs[0])
	for i := range strs {
		if len(strs[i]) < minLength {
			minLength = len(strs[i])
		}
	}
	for i := 0; i < minLength; i++ {
		currentChar := strs[0][i : i+1]
		for _, str := range strs {
			if str[i:i+1] != currentChar {
				return res.String()
			}
		}
		res.WriteString(currentChar)
	}
	return res.String()
}

func main() {
	fmt.Println(intToRoman(3))
	fmt.Println(intToRoman(50))
	fmt.Println(intToRoman(1994))
}
