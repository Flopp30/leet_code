class Solution:
    def intToRoman(self, num: int) -> str:
        dct = {1000: 'M',
               500: 'D',
               100: 'C',
               50: 'L',
               10: 'X',
               5: 'V',
               1: 'I'
               }
        roman_str = ''
        for key in dct.keys():
            if key > num:
                continue
            while num >= key:
                roman_str += dct[key]
                num -= key
        roman_str = roman_str.replace('VIIII', 'IX').replace('IIII', 'IV')
        roman_str = roman_str.replace('LXXXX', 'XC').replace('XXXX', 'XL')
        roman_str = roman_str.replace('DCCCC', 'CM').replace('CCCC', 'CD')
        return roman_str


for i in range(1000):
    a = Solution()
    print(a.intToRoman(i))
