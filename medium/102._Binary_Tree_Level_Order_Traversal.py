# Given the root of a binary tree, return the level order traversal of its nodes
# values. (i.e., from left to right, level by level).
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = list()
        temp_list = list()



