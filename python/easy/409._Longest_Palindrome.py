# Given a string s which consists of lowercase or uppercase letters, return the length
# of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1

class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        Time complexity O(n)
        Space complexity O(k), k - unique numbers count
        '''
        count_dict = {}
        for el in s:
            if el in count_dict:
                count_dict[el] += 1
            else:
                count_dict[el] = 1
        odd_counter, even_counter = 0, 0
        for el in count_dict.values():
            if el % 2 == 1:
                if odd_counter < el:
                    if odd_counter != 0:
                        even_counter += odd_counter - 1
                    odd_counter = el
                else:
                    even_counter += el - 1
            elif el % 2 == 0:
                even_counter += el
        return odd_counter + even_counter


if __name__ == '__main__':
    a = Solution()
    print(a.longestPalindrome('abccccdd'))
