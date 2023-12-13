# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majority_element(self, nums: list[int]) -> int:
        majority_count = len(nums) // 2
        for el_start, el_end in zip(nums, reversed(nums)):
            if nums.count(el_start) > majority_count:
                return el_start
            if nums.count(el_end) > majority_count:
                return el_end

    def majority_element_sort(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    a = Solution()
    print(a.majority_element([1, 2, 3, 1, 1]))
    print(a.majority_element_sort([1, 2, 3, 1, 1]))
