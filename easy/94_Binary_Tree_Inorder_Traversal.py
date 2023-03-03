# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Input: root = [1]
# Output: [1]
from typing import Optional, List, Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        '''
        Space O(1)
        Time O(n)
        '''

        def inorder(root: TreeNode | None) -> Iterator[TreeNode]:
            stack = [root] if root else []

            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    yield node
                    continue

                if node.right:
                    stack.append(node.right)
                stack.append(TreeNode(node.val))
                if node.left:
                    stack.append(node.left)

        return [node.val for node in inorder(root_)]
