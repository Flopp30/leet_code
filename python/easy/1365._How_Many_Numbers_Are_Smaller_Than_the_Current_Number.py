# Given the array nums, for each nums[i] find out how many numbers in the array
# are smaller than it. That is, for each nums[i] you have to count the number of
# valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.
#
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        Space O(n)
        Time O(n log n)
        '''
        res = []
        for idx in range(len(nums)):
            counter = 0
            for num in nums:
                if num < nums[idx]:
                    counter += 1
            res.append(counter)
        return res

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        '''
        Space O(n)
        Time O(n)
        :param nums:
        :return:
        '''
        temp = sorted(nums)
        hashmap = dict()
        res = list()
        for i in range(len(temp)):
            if temp[i] not in hashmap:
                hashmap[temp[i]] = i
        for i in range(len(nums)):
            res.append(hashmap[nums[i]])
        return res