# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

class Solution:
    def convert_to_title(self, column_number) -> str:
        return self.convert_to_title((column_number - 1) // 26) + \
               chr((column_number - 1) % 26 + ord('A')) if column_number else ''


a = Solution()
print(a.convert_to_title(30))
