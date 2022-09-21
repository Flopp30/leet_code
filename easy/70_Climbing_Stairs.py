# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Моё первое бинарное дерево (не судите строго!). Решение верное, но долго для больших значений
# counter__ = 0
#
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def tree_maker(self, n):
#         if n == 0:
#             global counter__
#             counter__ += 1
#             return
#         if n > 1:
#             self.left = TreeNode(n - 2)
#             self.left.tree_maker(n - 2)
#         self.right = TreeNode(n - 1)
#         self.right.tree_maker(n - 1)
#
#
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         global counter__
#         counter__ = 0
#         tree = TreeNode(n)
#         tree.tree_maker(n)
#         return counter__
# решение через цикл
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         lst = [0, 1, 2, 3]
#         if n < 4:
#             return lst[n]
#         for i in range(3, n + 1):
#             lst.append(lst[i] + lst[i - 1])
#         return lst[n]
from functools import lru_cache


class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


a = Solution()
print(a.climbStairs(50))
'''
1, 2, 3, 5, 8, 13, 21, 31 .. 
'''
