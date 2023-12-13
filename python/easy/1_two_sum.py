# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Space complexity O(n)
        Time complexity O(n)
        :param nums:
        :param target:
        :return:
        '''
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i

a = Solution()
print(a.twoSum([-1, -2, -3, -4, -5], -8))
