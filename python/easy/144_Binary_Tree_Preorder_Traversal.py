# Given the root of a binary tree, return the preorder traversal of its nodes' value
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#
# Input: root = [1]
# Output: [1]
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root:
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Space comp O(N)
        Time comp O(N)
        :param root:
        :return:
        '''
        res = list()
        queue = [root]
        while queue:
            current_node = queue.pop()
            res.append(current_node.val)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.left is not None:
                queue.append(current_node.left)
        return res
