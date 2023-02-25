# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
        Time complexity O(n)
        Space complexity O(n)
        :param numRows:
        :return:
        '''
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            prev_row = res[i - 1]
            temp = [1, *[prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)], 1]
            res.append(temp)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.generate(3))  # [[1], [1, 1], [1, 2, 1]]
