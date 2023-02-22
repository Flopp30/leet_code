# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        '''
        Space complexity O(1)
        Time complexity O(n)
        :param nums:
        :return:
        '''
        for idx, el in enumerate(nums):
            if idx == 0:
                continue
            nums[idx] += nums[idx-1]
        return nums


if __name__ == '__main__':
    a = Solution()
    print(a.runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
    print(a.runningSum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]
