# Given an integer number n, return the difference between the product of its digits and the sum of its digits
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
#
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        seq = list(map(int, (str(n))))
        mul_n = 1
        for el in seq:
            mul_n *= el
        return mul_n - sum(seq)
