# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        tmp = list()
        for el in s:
            if el in ('(', '[', '{'):
                tmp.append(el)
            else:
                try:
                    popped_el = tmp.pop()
                except IndexError:
                    return False
                if (el == ')' and popped_el == '(') or (el == ']' and popped_el == '[') or (
                        el == '}' and popped_el == '{'):
                    continue
                else:
                    return False
        return False if tmp else True


a = Solution()
print(a.isValid(s="(("))

# from collections import defaultdict
# class Solution:
#     def isValid(self, s: input_str) -> bool:
#         d = defaultdict(lambda: -1)
#         op = set("({[")
#         cl = set("]})")
#         d[')'] = '('
#         d['}'] = "{"
#         d[']'] = '['
#         stack = []
#
#         for i in s:
#             if i in op:
#
#                 stack.append(i)
#             elif stack:
#
#                 x = stack.pop(-1)
#                 if d[i] != x:
#                     return False
#
#             else:
#                 return False
#
#         return True if stack == [] else False
