# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.
# from typing import List
#
#
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) - 1
#         sum_ = (n * (n+1)) // 2
#         return sum_ - sum(nums)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 1:
            while n % 3 == 0:
                n //= 3
        return n == 1

a = Solution()
print(a.isPowerOfThree(45))