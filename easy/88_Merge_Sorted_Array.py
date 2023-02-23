# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
# that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        '''
        Space complexity O(1)
        Time complexity O(n + m)
        '''
        idx_1 = m - 1
        idx_2 = n - 1
        cursor = m + n - 1
        while idx_1 >= 0 and idx_2 >= 0:
            if nums1[idx_1] >= nums2[idx_2]:
                nums1[cursor] = nums1[idx_1]
                idx_1 -= 1
            else:
                nums1[cursor] = nums2[idx_2]
                idx_2 -= 1
            cursor -= 1
        while idx_1 >= 0:
            nums1[cursor] = nums1[idx_1]
            idx_1 -= 1
            cursor -= 1
        while idx_2 >= 0:
            nums1[cursor] = nums2[idx_2]
            idx_2 -= 1
            cursor -= 1


if __name__ == '__main__':
    a = Solution()

    nums1_ = [1, 2, 3, 0, 0, 0]
    a.merge(nums1_, m=3, nums2=[2, 5, 6], n=3)
    print(nums1_)  # 1 2 2 3 5 6
