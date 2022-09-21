class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        sum_ = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                sum_ += 4 * grid[i][j] + 2 if grid[i][j] else 0
                sum_ -= 2 * min(grid[i][j], grid[i + 1][j]) if i < len(grid) - 1 else 0
                sum_ -= 2 * min(grid[i][j], grid[i][j + 1]) if j < len(grid) - 1 else 0
        return sum_


a = Solution()
print(a.surfaceArea([[1, 2], [3, 4]]))
