# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for slow in range(len(nums) - 1):
            for fast in range(slow + 1, len(nums)):
                if nums[slow] == nums[fast]:
                    c += 1
        return c

if __name__ == '__main__':
    a = Solution()
    print(a.numIdenticalPairs([1, 1, 1, 1]))
