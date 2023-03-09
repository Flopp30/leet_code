# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
# is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces,
# square brackets are well-formed, etc. Furthermore, you may assume that the original data
# does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(idx):
            ans = ""
            while idx < len(s) and s[idx] != ']':
                while idx < len(s) and s[idx].isalpha():
                    ans += s[idx]
                    idx += 1
                if idx >= len(s) or s[idx] == ']':
                    continue
                n = ""
                while idx < len(s) and s[idx].isdigit():
                    n += s[idx]
                    idx += 1
                tmp, idx = decode(idx + 1)
                ans += tmp * int(n)
            return ans, idx + 1

        return decode(0)[0]


if __name__ == '__main__':
    a = Solution()
    print(a.decodeString("2[abc]3[cd]ef"))
