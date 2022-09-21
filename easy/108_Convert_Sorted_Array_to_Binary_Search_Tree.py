# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees
# of every node never differs by more than one.
from statistics import median


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        total_nums = len(nums)
        if not total_nums:
            return None
        return TreeNode(nums[total_nums // 2], self.sortedArrayToBST(nums[:total_nums // 2]),
                        self.sortedArrayToBST(nums[total_nums // 2 + 1:]))
