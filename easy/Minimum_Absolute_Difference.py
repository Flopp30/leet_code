# Given an array of distinct integers lst, find all pairs of elements
# with the minimum absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from lst
# a < b
# b - a equals to the minimum absolute difference of any two elements in lst

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr = sorted(arr)
        diff = abs(arr[0] - arr[1])
        result = list()
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < diff:
                diff = abs(arr[i] - arr[i + 1])
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == diff:
                result.append([arr[i], arr[i + 1]])
        return result


a = Solution()
print(a.minimumAbsDifference([40, 11, 26, 27, -20]))
