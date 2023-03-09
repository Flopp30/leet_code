# Given the root of a binary search tree and an integer k,
# return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        '''
        Space O(n)
        Time O(n)
        '''
        hashmap = {}
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            diff = k - node.val
            if diff in hashmap:
                return True
            hashmap[node.val] = diff
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
