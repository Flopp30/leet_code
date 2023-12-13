# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Input: s = "()"
# Output: true
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "(]"
# Output: false
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time complexity O(n)
        Space complexity O(n/2)
        '''
        stack = list()
        opn = set('({[')
        close = set(')}]')
        for el in s:
            if el in opn:
                stack.append(el)
            if el in close:
                if stack:
                    last_el = stack.pop()
                    if el == ']' and last_el == '[':
                        continue
                    elif el == '}' and last_el == '{':
                        continue
                    elif el == ')' and last_el == '(':
                        continue
                return False

        return False if stack else True
