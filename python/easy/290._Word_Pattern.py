# https://leetcode.com/problems/word-pattern/description/
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_mapping = dict()
        words_mapping = dict()
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for pat, el in zip(pattern, words):
            if pat not in pattern_mapping:
                pattern_mapping[pat] = el

            elif pattern_mapping[pat] != el:
                return False

            if el not in words_mapping:
                words_mapping[el] = pat

            elif words_mapping[el] != pat:
                return False

        return True
