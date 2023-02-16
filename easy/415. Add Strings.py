# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library
# for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.
#
# Example 1:
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
from itertools import zip_longest


class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        '''
        Time complexity O(max(N, M))
        Space Complexity: O(max(N,M))
        :param num1:
        :param num2:
        :return:
        '''
        res = []
        i_1 = len(num1)
        i_2 = len(num2)
        carry = 0
        while i_1 or i_2 or carry:
            if i_1:
                carry += ord(num1[i_1 - 1]) - ord('0')
                i_1 -= 1
            if i_2:
                carry += ord(num2[i_2 - 1]) - ord('0')
                i_2 -= 1

            res.append(chr(carry % 10 + ord('0')))
            carry //= 10
        return ''.join(res[::-1])


a = Solution()
print(a.add_strings('999', '123'))
