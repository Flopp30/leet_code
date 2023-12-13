# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving
# the order of characters. No two characters may map to the same character, but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Time complexity O(n)
        Space complexity O(k) - k is the number of unique character in S and T
        '''
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for el_s, el_t in zip(s, t):
            if el_s in hashmap_s:
                if hashmap_s[el_s] != el_t:
                    return False
            else:
                if el_t in hashmap_t:
                    return False
                hashmap_s[el_s] = el_t
                hashmap_t[el_t] = el_s
        return True


if __name__ == '__main__':
    a = Solution()
    print(a.isIsomorphic('badc', 'baba'))
    print(a.isIsomorphic('paper', 'title'))
