# You are given the root node of a binary search tree (BST) and a value
# to insert into the tree. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
#
# Notice that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
#
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
#
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Space comp O(N)
        Time comp O(N)
        :param root:
        :param val:
        :return:
        '''
        head = root
        if root.val < val:
            queue = [head.left]
        else:
            queue = [head.right]
        while queue:
            node = queue.pop()
            if node:
                if node.val > val:
                    if node.left:
                        queue.append(node.left)
                        continue
                    else:
                        node.left = TreeNode(val)
                        return root
                else:
                    if node.right:
                        queue.append(node.right)
                        continue
                    else:
                        node.right = TreeNode(val)
                        return root
        return root

    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

