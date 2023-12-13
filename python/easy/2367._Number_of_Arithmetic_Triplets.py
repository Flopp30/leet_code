# https://leetcode.com/problems/number-of-arithmetic-triplets/
# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
#
# Return the number of unique arithmetic triplets.
#
# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.
#
# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        '''
        Space comp O(1)
        Time comp O(n * log n * log log n)
        :param nums:
        :param diff:
        :return:
        '''
        i, j, k, res = 0, 0, 0, 0
        while i != len(nums) - 2:
            while j != len(nums) - 1:
                while k != len(nums):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        res += 1
                    k += 1
                j += 1
                k = j + 1
            i += 1
            j = i + 1
            k = j + 1
        return res

    def arithmeticTriplets2(self, nums: List[int], diff: int) -> int:
        '''
        Space O(1)
        Time O(n ^ 2)
        '''
        res = 0
        for num in nums:
            if num + diff in nums and num + 2 * diff in nums:
                res += 1
        return res
