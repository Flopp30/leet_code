# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string ""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        tmp = strs[0]
        strs.sort(key=len)
        result = ''
        for word in strs:
            result = ''
            for sym_pref, sym_el in zip(tmp, word):
                if sym_el == sym_pref:
                    result += sym_el
                else:
                    break
            tmp = result
        return result


a = Solution()
print(a.longestCommonPrefix(["aa", "ab"]))
