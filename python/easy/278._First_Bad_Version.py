# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

from random import choice


def isBadVersion(version: int) -> bool:
    return choice((True, False))


class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        Space comp O(1)
        Time comp O(N * log(N)
        :param n:
        :return:
        '''
        left = 1
        right = n
        while left <= right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid - 1
                if not isBadVersion(right):
                    return right
            else:
                left = mid + 1
