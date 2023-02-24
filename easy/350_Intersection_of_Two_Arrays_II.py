# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        '''
        Time complexity - O(max(N, M) + K),
        N - len(nums1), M - len(nums2),
        K - maximum number of duplicates in the intersection of lists
        Space Complexity O(N+M)
        '''
        res = []
        hashmap_1 = Counter(nums1)
        hashmap_2 = Counter(nums2)
        for key in hashmap_1.keys():
            if key in hashmap_2:
                for _ in range(max(hashmap_1[key], hashmap_2[key])):
                    res.append(key)
        return res


if __name__ == "__main__":
    a = Solution()
    a.intersect([1, 2, 2, 1], [2, 2])
