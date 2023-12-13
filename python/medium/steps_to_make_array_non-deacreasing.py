# You are given a 0-indexed integer array nums.
# In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
#
# Return the number of steps performed until nums becomes a non-decreasing array.


class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        result = 0
        length_nums = len(nums)
        stack = [[nums[-1], 0]]

        for i in reversed(range(length_nums - 1)):
            count = 0
            while stack and stack[-1][0] < nums[i]:
                count = max(count + 1, stack.pop()[1])
            result = max(result, count)
            stack.append([nums[i], count])

        return result


a = Solution()
print(a.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
