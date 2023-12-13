# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on
# the image starting from the pixel image[sr][sc].
# 
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
# to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
# to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with color.
# 
# Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        '''
        Space complexity O(2N)
        Time complexity O(N log n)
        :param image:
        :param sr:
        :param sc:
        :param color:
        :return:
        '''
        if not image:
            return [[]]
        length, width = len(image) - 1, len(image[0]) - 1
        queue = list()
        completed_dot = dict()
        if sr <= length and sc <= width:
            queue.append((sr, sc))
            target_color = image[sr][sc]
        while queue:
            sr, sc = queue.pop()
            if image[sr][sc] == target_color:
                image[sr][sc] = color
                if (sr, sc) not in completed_dot:
                    if sr - 1 >= 0:
                        queue.append([sr - 1, sc])
                    if sr + 1 <= length:
                        queue.append([sr + 1, sc])
                    if sc + 1 <= width:
                        queue.append([sr, sc + 1])
                    if sc - 1 >= 0:
                        queue.append([sr, sc - 1])
            completed_dot[(sr, sc)] = 1

        return image


if __name__ == '__main__':
    a = Solution()
    print(a.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
