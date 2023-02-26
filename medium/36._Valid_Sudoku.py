# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        '''
        Time complexity O(1)
        Space complexity O(1)
        :param board:
        :return:
        '''
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == '.':
                    continue
                if (current in rows[i]) or (current in cols[j]) or (current in block[i // 3][j // 3]):
                    return False
                rows[i].add(current)
                cols[j].add(current)
                block[i // 3][j // 3].add(current)
        return True
