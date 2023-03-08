# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1
            cur_len = r - l + 1
            if cur_len - max(freq.values()) <= k:
                maxlen = max(maxlen, cur_len)
            else:
                freq[s[l]] -= 1
                l += 1

        return maxlen
