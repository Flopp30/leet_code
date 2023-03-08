# Given the root of a binary tree, invert the tree, and return its root.
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Input: root = [2,1,3]
# Output: [2,3,1]
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Space O(n)
        Time O(n)
        :param root:
        :return:
        '''
        queue = [root] if root else []
        while queue:
            cur_el = queue.pop()
            cur_el.left, cur_el.right = cur_el.right, cur_el.left
            if cur_el.left:
                queue.append(cur_el.left)
            if cur_el.right:
                queue.append(cur_el.right)
        return root

