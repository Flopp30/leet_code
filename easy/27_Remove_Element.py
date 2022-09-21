# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally,
# if there are k elements after removing the duplicates, then the first k elements of nums
# should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the
# input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         anchor = 0
#         while anchor < len(nums):
#             if nums[anchor] != val:
#                 break
#             anchor += 1
#         if anchor == len(nums):
#             return 0
#         nums[0], nums[anchor] = nums[anchor], nums[0]
#         anchor = 0
#         walker = 1
#         while walker < len(nums):
#             if nums[walker] != val:
#                 nums[anchor + 1], nums[walker] = nums[walker], nums[anchor + 1]
#                 anchor += 1
#             walker += 1
#         return anchor + 1

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[anchor] = nums[i]
                anchor += 1

        i = anchor
        while i < len(nums):
            nums[i] = '_'
            i += 1

        return anchor


a = Solution()
print(a.removeElement(nums=[3, 2, 2, 3], val=3))
