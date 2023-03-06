# Given the root of a binary tree and an integer targetSum, return true if the tree
# has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.val == targetSum and root.right is None and root.left is None:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        cur_sum = root.val
        queue = [(cur_sum, root)]
        while queue:
            cur_sum, node = queue.pop()
            cur_sum += node.val
            if cur_sum == targetSum:
                return True
            elif cur_sum > targetSum:
                return False
            if node.left:
                queue.append((cur_sum, node.left))
            if node.right:
                queue.append((cur_sum, node.right))

        return False
