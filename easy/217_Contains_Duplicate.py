# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        Space complexity O(n)
        Time complexity O(n)
        :param nums:
        :return:
        '''
        hash_t = {}
        for el in nums:
            if el in hash_t:
                return True
            hash_t[el] = 1
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1, 2, 3, 1]))  # True
    print(a.containsDuplicate([1, 2, 3, 4]))  # False
    print(a.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
