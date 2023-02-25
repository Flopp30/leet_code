# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one
# with a different size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number
# of columns of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix
# in the same row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
# Otherwise, output the original matrix.
#
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        '''
        Space complexity: O(n)
        Time complexity: O(n * m), where n - length matrix, m - length element matrix
        '''
        if len(mat) * len(mat[0]) != r * c:
            return mat
        new_mat = []
        stash = []
        el_counter = 0
        for row in mat:
            for el in row:
                stash.append(el)
                el_counter += 1
                if el_counter == c:
                    new_mat.append(stash)
                    stash = list()
                    el_counter = 0
        return new_mat
    
    def matrixReshape2(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        flat, ans = [], []
        for i in mat:
            flat += i
        for i in range(r):
            ans += [flat[i * c:i * c + c]]
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.matrixReshape2([[1, 2], [3, 4]], 4, 1))
