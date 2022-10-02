# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        tree_values = list()
        if root is None:
            return tree_values
        tree_values.append(root.val)
        tree_values += self.preorderTraversal(root.left)
        tree_values += self.preorderTraversal(root.right)

        return tree_values
