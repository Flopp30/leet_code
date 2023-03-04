# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        '''
        Time complexity  O(n)
        Space complexity O(1)
        '''
        if not root:
            return False
        left_queue = [root.left]
        right_queue = [root.right]
        while left_queue and right_queue:
            left_n = left_queue.pop()
            right_n = right_queue.pop()
            if left_n and right_n:
                if left_n.val != right_n.val:
                    return False
                left_queue.extend((left_n.left, left_n.right))
                right_queue.extend((right_n.right, right_n.left))
            elif left_n is None and right_n is None:
                continue
            else:
                return False
        return True
