# Given an integer num, return the number of digits in num that divide num.
#
# An integer val divides nums if nums % val == 0
#
# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        seq = str(num)
        for el in seq:
            if num % int(el) == 0:
                counter += 1
        return counter
