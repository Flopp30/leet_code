# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Space comp O(2N)
        Time comp O(n)
        '''
        if len(s) != len(t):
            return False
        frequency_s, frequency_t = {}, {}
        for i in range(len(s)):
            frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1
            frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
        return frequency_s == frequency_t


if __name__ == '__main__':
    a = Solution()
    print(a.isAnagram("anagram", "nagaram"))
    print(a.isAnagram("a", "ab"))
