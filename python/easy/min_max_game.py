# You are given a 0-indexed integer array nums whose length is a power of 2.
#
# Apply the following algorithm on nums:
#
# Let n be the length of nums. If n == 1, end the process.
# Otherwise, create a new 0-indexed integer array newNums of length n / 2.
# For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
# For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.

class Solution:

    @staticmethod
    def min_max_game(nums: list[int]):
        min_max = 'min'
        while len(nums) != 1:
            new_array = list()
            for i in range(0, len(nums) - 1, 2):
                if min_max == 'min':
                    new_array.append(min(nums[i], nums[i + 1]))
                    min_max = 'max'
                    continue
                new_array.append(max(nums[i], nums[i + 1]))
                min_max = 'min'
            nums = new_array
        return nums


a = Solution()
print(a.min_max_game([1, 3, 5, 2, 4, 8, 2, 2]))
