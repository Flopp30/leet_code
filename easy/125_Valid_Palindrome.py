# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_str = ''
#         for el in s:
#             if el.isalpha() or el.isdigit():
#                 new_str += el.lower()
#         return True if new_str[::-1] == new_str else False


# решение через re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^0-9a-z]+', "", s.lower())
        return s == s[::-1]


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
