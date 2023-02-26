# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Binary Search
        row, col = len(matrix), len(matrix[0])
        i, j = 0, (row * col) - 1

        while i <= j:
            mid = (i + j) >> 1
            mid_element = matrix[mid // col][mid % col]
            if mid_element == target:
                return True
            elif mid_element < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))