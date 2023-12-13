# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that
# the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
#
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
# Input: m = 3, n = 7
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def give_unique_path(i, j):
            if i == 0 or j == 0:
                return 0
            if i == 1 and j == 1:
                return 1
            return give_unique_path(i - 1, j) + give_unique_path(i, j - 1)

        answ = give_unique_path(m, n)
        return answ

    def uniquePaths2(self, m: int, n: int) -> int:
        '''
        Space comp O(n*m)
        Time comp O(n*m)
        '''
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i][j - 1] + memo[i - 1][j]

        return memo[-1][-1]


if __name__ == '__main__':
    a = Solution()
    print(a.uniquePaths(3, 2))
