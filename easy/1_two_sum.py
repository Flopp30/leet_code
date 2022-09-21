# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = list()
        for el in nums:
            if (el <= target or el >= target) and (target - el) in nums:
                if el == (target - el) and nums.count(el) == 1:
                    continue
                elif el == (target - el) and nums.count(el) == 2:
                    result.append(nums.index(el))
                    nums[nums.index(el)] = el + 1
                    result.append(nums.index(target - el))
                    break
                else:
                    result = [nums.index(el), nums.index(target - el)]
                    break
        return result


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i

a = Solution()
print(a.twoSum([-1, -2, -3, -4, -5], -8))
