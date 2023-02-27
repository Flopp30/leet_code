# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Input: s = "leetcode"
# Output: 0
#
# Input: s = "loveleetcode"
# Output: 2
#
# Input: s = "aabb"
# Output: -1
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Space comp O(1)
        Time comp O(n^2)
        '''
        for idx, el in enumerate(s):
            if s.count(el) == 1:
                return idx
        return -1

    def firstUniqCharV2(self, s: str) -> int:
        '''
        Space comp O(n)
        Time comp O(n)
        '''
        if 1 not in Counter(s).values():
            return -1
        for i, j in Counter(s).items():
            if j == 1:
                return s.index(i)
