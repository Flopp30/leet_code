class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
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