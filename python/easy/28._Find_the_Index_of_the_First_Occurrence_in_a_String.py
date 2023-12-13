# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, len(needle) - 1
        while p1 <= len(haystack) - len(needle):
            if haystack[p1] == needle[0] and haystack[p1 + p2] == needle[p2] and haystack[p1:p1 + p2 + 1] == needle:
                return p1
            p1 += 1
        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.strStr('a', 'a'))
