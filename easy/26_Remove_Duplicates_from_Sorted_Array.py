# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        anchor, walker = 0, 1
        while walker < len(nums):
            if nums[walker] != nums[anchor]:
                nums[anchor + 1] = nums[walker]
                anchor += 1
            walker += 1
        return anchor + 1


a = Solution()
print(a.removeDuplicates([-1, -1, 0, 0, 0, 3, 3]))
