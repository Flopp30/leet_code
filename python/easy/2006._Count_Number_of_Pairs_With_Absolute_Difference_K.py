# Given an integer array nums and an integer k, return the number of pairs (i, j)
# where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.
#
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        '''
        Space O(1)
        Time O(n log n)
        '''
        res, p1, p2 = 0, 0, 1
        while p1 != len(nums):
            while p2 != len(nums):
                if abs(nums[p1] - nums[p2]) == k:
                    res += 1
                p2 += 1
            p1 += 1
            p2 = p1 + 1
        return res

    def countKDifference2(self, nums: List[int], k: int) -> int:
        '''
        Space O(n)
        Time O(n)
        '''
        hashmap, res = {}, 0
        for num in nums:
            if k - num in hashmap:
                res += hashmap[k - num]
            if k + num in hashmap:
                res += hashmap[k + num]
            hashmap[num] += 1
        return res
