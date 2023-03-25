# https://leetcode.com/problems/spiral-matrix/
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        while matrix:
            res += matrix.pop(0)

            if matrix and matrix[0]:
                for line in matrix:
                    res.append(line.pop())

            if matrix:
                res += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for line in matrix[::-1]:
                    res.append(line.pop(0))

        return res
