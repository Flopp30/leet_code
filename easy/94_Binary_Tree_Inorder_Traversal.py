# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
#
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list[int]:
#         result = list()
#
#         def rec(node):
#
#             if node.left:
#                 rec(node.left)
#             result.append(node.val)
#             if node.right:
#                 rec(node.right)
#
#         if root:
#             rec(root)
#
#         return result

# [1, null, 2, 3]
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = list()
        stack = list()
        temp = root
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            last = stack.pop()
            result.append(last.val)
            temp = last.right

        return result


a = Solution()
print(a.inorderTraversal([1, 2, 3]))
