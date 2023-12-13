# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return 1

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if left == 0 or right == 0 or abs(left - right) > 1:
            return False

        return max(left, right) + 1
