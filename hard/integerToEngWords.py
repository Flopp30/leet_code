dct = {1000000000: 'Billion', 1000000: 'Million', 1000: 'thousand', 100: 'Hundred',
       90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty',
       30: 'Thirty', 20: 'Twenty', 19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen',
       15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen', 12: 'Twelve', 11: 'Eleven', 10: 'Ten',
       9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four', 3: 'Three', 2: 'Two', 1: 'One'
       }

class Solution:
    def numberToWords(self, num: int) -> str:
        return_str = ''
        if num in dct.keys():
            return dct[num]
        temp = 0


def rec_func(num, rslt_sct):
    pass



a = Solution()
print(a.numberToWords(39101))