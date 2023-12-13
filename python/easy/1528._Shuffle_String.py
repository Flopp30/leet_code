# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.
#
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        '''
        Space O(n)
        Time O(n log n)
        '''
        hashmap = {idx: el for idx, el in zip(indices, s)}
        return ''.join((map(lambda x: x[1], sorted(hashmap.items()))))

    def restoreString2(self, s: str, indices: List[int]) -> str:
        '''
        Space O(n)
        Time O(n)
        '''
        res = ['' for _ in range(len(s))]
        for idx, el in zip(indices, s):
            res[idx] = el
        return ''.join(res)


a = Solution()
print(a.restoreString('codeleet', indices=[4, 5, 6, 7, 0, 2, 1, 3]))
