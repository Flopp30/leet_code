# There are n people that are split into some unknown number of groups.
# Each person is labeled with a unique ID from 0 to n - 1.
#
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
# For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
#
# Return a list of groups such that each person i is in a group of size groupSizes[i].
#
# Each person should appear in exactly one group, and every person must be in a group.
# If there are multiple answers, return any of them. It is guaranteed that there will be
# at least one valid solution for the given input.
#
# Input: groupSizes = [2, 1, 3, 3, 3, 2]
# Output: [[1], [0, 5], [2, 3, 4]]
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        Space O(n + k)
        Time O(n log n)
        :param groupSizes:
        :return:
        '''
        hashmap = {}
        res = list()
        temp = list()
        for idx, el in enumerate(groupSizes):
            if el in hashmap:
                hashmap[el].append(idx)
            else:
                hashmap[el] = [idx]
        for key, items in hashmap.items():
            for item in items:
                temp.append(item)
                if len(temp) == key:
                    res.append(temp)
                    temp = list()
        return res

    def groupThePeople2(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        Space O(n)
        Time O(n)
        :param groupSizes:
        :return:
        '''
        hashmap = {}
        res = list()
        for idx, el in enumerate(groupSizes):
            if el in hashmap:
                hashmap[el].append(idx)
            else:
                hashmap[el] = [idx]
            if len(hashmap[el]) == el:
                res.append(hashmap[el])
                del hashmap[el]
        return res


