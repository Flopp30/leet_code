# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
#
# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
#
# leftSum[i] is the sum of elements to the left of the index i in the array nums.
# If there is no such element, leftSum[i] = 0.
#
# rightSum[i] is the sum of elements to the right of the index i in the array nums.
# If there is no such element, rightSum[i] = 0.
# Return the array answer.
#
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
#
# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        '''
        space O(1)
        time O(n)
        :param nums:
        :return:
        '''
        left_sum = 0
        right_sum = sum(nums)
        for idx in range(len(nums)):
            tmp = nums[idx]
            right_sum -= tmp
            nums[idx] = abs(left_sum - right_sum)
            left_sum += tmp
        return nums


if __name__ == '__main__':
    a = Solution()
    print(a.leftRigthDifference([10, 4, 8, 3]))
