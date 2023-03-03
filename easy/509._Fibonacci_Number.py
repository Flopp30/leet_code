# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

class Solution:
    def fib(self, n: int) -> int:
        '''
        Space complexity O(
        Time complexity O(
        :param n:
        :return:
        '''
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    a = Solution()
    print(a.fib(10))
