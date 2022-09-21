# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         def rec(root_, depth):
#             if not root_:
#                 return depth
#             if not root_.left:
#                 return rec(root_.right, depth + 1)
#             if not root_.right:
#                 return rec(root_.left, depth + 1)
#             return min(rec(root_.left, depth + 1), rec(root_.right, depth +1))
#         return rec(root, 0)


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return 1

        left = self.minDepth(root.left) if root.left else float('inf')
        right = self.minDepth(root.right) if root.right else float('inf')
        return 1 + min(left, right)

