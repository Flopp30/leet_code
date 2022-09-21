# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         if numRows == 1:
#             res = [[1]]
#         if numRows >= 2:
#             res = [[1], [1, 1]]
#         while numRows > 2:
#             new_row = [1, [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)], 1]
#             res.append(new_row)
#             numRows -= 1
# #         return res
# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         if numRows == 1:
#             res = [[1]]
#         if numRows >= 2:
#             res = [[1], [1, 1]]
a= 5
print('ghbdn' + a)
