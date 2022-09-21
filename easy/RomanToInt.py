class Solution:
    def roman_to_int(self, s: str) -> int:
        dct = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        result_int = 0
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')

        for i in range(len(s)):
            result_int += dct[s[i]]

        return result_int


a = Solution()
print(a.roman_to_int('XXXI'))
