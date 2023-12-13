# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        counter = 0
        while i <= len(nums):
            if nums[i] == 0:
                del nums[i]
                counter += 1
                continue
            i += 1
        nums.extend([0] * counter)
