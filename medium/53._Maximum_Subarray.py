# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.
#
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray[4, -1, 2, 1] has the largest sum 6.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        '''
        Space complexity O(1)
        Time complexity O(n)
        :param nums:
        :return:
        '''
        max_sum = current_sum = nums[0]
        for idx in range(1, len(nums)):
            current_sum += nums[idx]

            if current_sum < nums[idx]:
                current_sum = nums[idx]

            if current_sum > max_sum:
                max_sum = current_sum

        return max(max_sum, current_sum)


if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(a.maxSubArray([5, 4, -1, 7, 8]))  # 23
    print(a.maxSubArray([1, 2]))  # 3
