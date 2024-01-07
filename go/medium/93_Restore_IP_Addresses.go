package main

import (
	"fmt"
	"strings"
)

// A valid IP address consists of exactly four integers separated by single dots.
//
//	Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
//
// For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
// but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
// Given a string s containing only digits, return all possible valid IP addresses that can
// be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s.
// You may return the valid IP addresses in any order.
// Example 1:
// Input: s = "25525511135"
// Output: ["255.255.11.135","255.255.111.35"]
//
// Example 2:
// Input: s = "0000"
// Output: ["0.0.0.0"]
//
// Example 3:
// Input: s = "101023"
// Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
func restoreIpAddresses(s string) []string {
	var ans []string
	helper(s, 4, []string{}, &ans)
	return ans
}

func helper(s string, remain int, current []string, ans *[]string) {
	if remain == 0 {
		if len(s) != 0 {
			return
		}
		if valid(s) {
			current = append(current, s)
		}
		if len(current) == 4 {
			tmp := strings.Join(current, ".")
			*ans = append(*ans, tmp)
		}
		return
	}
	if len(s) >= 1 && valid(s[:1]) {
		helper(s[1:], remain-1, append(current, s[:1]), ans)
	}
	if len(s) >= 2 && valid(s[:2]) {
		helper(s[2:], remain-1, append(current, s[:2]), ans)
	}
	if len(s) >= 3 && valid(s[:3]) {
		helper(s[3:], remain-1, append(current, s[:3]), ans)
	}
}

func valid(str string) bool {
	if len(str) > 1 && str[0] == '0' {
		return false
	}
	if len(str) == 1 {
		return str >= "0" && str <= "9"
	}
	if len(str) == 2 {
		return str >= "10" && str <= "99"
	}
	if len(str) == 3 {
		return str >= "100" && str <= "255"
	}
	return false
}
func main() {
	fmt.Println(restoreIpAddresses("25525511135"))
	fmt.Println(restoreIpAddresses("0000"))
	fmt.Println(restoreIpAddresses("101023"))
}
