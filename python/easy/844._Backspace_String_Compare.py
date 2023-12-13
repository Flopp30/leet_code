# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        Space comp max(len(s), len(t))
        Time comp O(max(len(s), len(t))
        '''
        def solve(string):
            res = list()
            for symbol in string:
                if symbol == '#':
                    if res:
                        res.pop()
                else:
                    res.append(symbol)
            return ''.join(res)
        return solve(s) == solve(t)


if __name__ == '__main__':
    a = Solution()
    print(a.backspaceCompare(s="ab##", t="d#c#"))
