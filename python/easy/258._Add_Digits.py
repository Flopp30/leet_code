# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            temp = 0
            while num != 0:
                temp += num % 10
                num //= 10
            if temp < 10:
                return temp
            num = temp