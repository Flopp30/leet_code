# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for idx, el in enumerate(nums):
            if el in hashmap:
                if idx - hashmap[el] <= k:
                    return True
                else:
                    hashmap[el] = idx
            else:
                hashmap[el] = idx
        return False
