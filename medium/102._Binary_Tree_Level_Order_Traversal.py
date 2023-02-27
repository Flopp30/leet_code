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
        '''
        Time comp O(n)
        Space O(2n)
        :param root:
        :return:
        '''
        if not root:
            return None
        queue, res = [root], []
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                curr_node = queue.pop(0)
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(level)
        return res

