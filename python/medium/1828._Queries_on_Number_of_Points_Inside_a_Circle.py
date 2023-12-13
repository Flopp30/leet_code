# You are given an array points where points[i] = [xi, yi] is the coordinates
# of the ith point on a 2D plane. Multiple points can have the same coordinates.
#
# You are also given an array queries where queries[j] = [xj, yj, rj] describes
# a circle centered at (xj, yj) with a radius of rj.
#
# For each query queries[j], compute the number of points inside the jth circle.
# Points on the border of the circle are considered inside.
#
# Return an array answer, where answer[j] is the answer to the jth query.
#
# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]
# Explanation: The points and circles are shown above.
# queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.
#
# Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# Output: [2,3,2,4]
# Explanation: The points and circles are shown above.
# queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.
#
# 1 <= points.length <= 500
# points[i].length == 2
# 1 <= queries.length <= 500
# queries[j].length == 3
# 0 <= xj, yj <= 500
# 1 <= rj <= 500
# All coordinates are integers.
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        '''
        Space O(n+k)
        Time O(n+k)
        '''
        answer = []
        counter = 0
        for query in queries:
            x, y, r = query
            for point in points:
                a, b = point
                if (x - a) * (x - a) + (y - b) * (y - b) <= r * r:
                    counter += 1
            answer.append(counter)
            counter = 0
        return answer


if __name__ == '__main__':
    a = Solution()
    print(a.countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
