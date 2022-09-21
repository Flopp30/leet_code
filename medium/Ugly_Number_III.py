# An ugly number is a positive integer that is divisible by a, b, or c.
#
# Given four integers n, a, b, and c, retur n the nth ugly number.

class Solution:

    @staticmethod
    def gen_ugly_numbers(a_, b_, c_):
        for i in range(min(a_, b_, c_), 2 * 10 ** 9):
            if i % a_ == 0 or i % b_ == 0 or i % c_ == 0:
                yield i

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        return min(a,b,c) * n


solu = Solution()
print(solu.nthUglyNumber(n=10000000, a=2, b=217983653, c=336916467))
