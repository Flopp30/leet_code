# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path '
# from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Input: root = [1,null,2]
# Output: 2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        '''
        Space complexity O(n)
        Time complexity O(n)
        '''
        depth = 1 if root else 0
        queue = [(depth, root)] if root else []
        while queue:
            level, node = queue.pop()
            if node.left or node.right:
                level += 1
                depth = max(depth, level)
                if node.left:
                    queue.append((level, node.left))
                if node.right:
                    queue.append((level, node.right))
        return depth
