# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# class Solution:
#
#     def isPalindrome(self, x: int) -> bool:
#         if input_str(x) == input_str(x)[::-1]:
#             return True
#         return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        x_copy = x
        while x_copy != 0:
            rev, x_copy = rev * 10 + x_copy % 10, x_copy // 10
        if rev == x:
            return True
        return False


a = Solution()
print(a.isPalindrome(110))