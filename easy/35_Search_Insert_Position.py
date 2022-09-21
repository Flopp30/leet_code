# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
# Broot force
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         if target <= nums[0]:
#             return 0
#         for i in range(len(nums) - 1):
#             if nums[i] <= target <= nums[i + 1]:
#                 return i + 1
#         if target >= nums[-1]:
#             return len(nums)

# Binary search
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        if nums[n - 1] < target:
            return len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return low


a = Solution()
print(a.searchInsert(nums=[1, 3, 5, 7], target=6))
