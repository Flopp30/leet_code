# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        val_list1 = list()
        if not p and not q:
            return True
        if not p or not q:
            return False

        def rec(node: TreeNode):
            if node.left:
                val_list1.append('left')
                rec(node.left)
            val_list1.append(node.val)
            if node.right:
                val_list1.append('right')
                rec(node.right)
        rec(p)
        val_list2 = val_list1[:]
        val_list1 = list()
        rec(q)
        return True if val_list2 == val_list1 else False

# решение без рекурсии
# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         stack1 = [];
#         stack1.append(p)
#         stack2 = [];
#         stack2.append(q)
#
#         while len(stack1) and len(stack2):
#             node1 = stack1.pop(0)
#             node2 = stack2.pop(0)
#             if (not node1 and node2) or (node1 and not node2):
#                 return False
#             elif not node1 and not node2:
#                 continue
#             elif node1.val != node2.val:
#                 return False
#             stack1.append(node1.left)
#             stack1.append(node1.right)
#             stack2.append(node2.left)
#             stack2.append(node2.right)
#         return True
