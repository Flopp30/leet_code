# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# без рекурсии
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root.left and not root.right:
#             return True
#         if (not root.left and root.right) or (root.left and not root.right):
#             return False
#         stack_left = list()
#         stack_left.append(root.left)
#         stack_right = list()
#         stack_right.append(root.right)
#         while stack_right or stack_left:
#             el_left = stack_left.pop()
#             el_right = stack_right.pop()
#             if el_left.val == el_right.val:
#                 if el_left.left and el_right.right:
#                     stack_left.append(el_left.left)
#                     stack_right.append(el_right.right)
#                 elif not el_left.left and not el_right.right:
#                     pass
#                 else:
#                     return False
#                 if el_left.right and el_right.left:
#                     stack_left.append(el_left.right)
#                     stack_right.append(el_right.left)
#                 elif not el_left.right and not el_right.left:
#                     pass
#                 else:
#                     return False
#             else:
#                 return False
#         return True

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

