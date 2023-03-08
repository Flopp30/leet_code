# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
#
# You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]
# Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Space O(1) - max len = 26 char
        Time O(n)
        :param s:
        :param p:
        :return:
        '''
        char_hashmap, indices, len_p, len_s = defaultdict(int), [], len(p), len(s)

        # s cannot have p anangrams if len(p) > len(s)
        if len_p > len_s:
            return indices

        # build map of character frequencies in p
        for char in p:
            char_hashmap[char] += 1

        # initial full pass over the window, except last element which we will pass over later
        for i in range(len_p - 1):
            if s[i] in char_hashmap:
                char_hashmap[s[i]] -= 1

        # slide the window with stride 1, adding the value "sliding out" and subtracting the value "sliding in"
        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in char_hashmap:
                char_hashmap[s[i]] += 1
            if i + len_p < len_s and s[i + len_p] in char_hashmap:
                char_hashmap[s[i + len_p]] -= 1

            # check whether we encountered an anagram by seeing if all frequencies add up to 0
            if not any(char_hashmap.values()):
                indices.append(i + 1)

        return indices


if __name__ == '__main__':
    a = Solution()
    print(a.findAnagrams(s="abab", p="ab"))
    print(a.findAnagrams(s="abceeeeacbacacaab", p="abc"))
