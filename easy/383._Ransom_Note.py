# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
#
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Space complexity O(k),  k - count of unique number
        Time complexity O(n^2)
        '''
        letters_set = set(ransomNote)
        for el in letters_set:
            if ransomNote.count(el) <= magazine.count(el):
                continue
            return False
        return True
