# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1


a = Solution()
print(a.search([-1, 0, 3, 5, 9, 12], 9))
