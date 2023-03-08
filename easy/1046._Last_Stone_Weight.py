# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
#
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
#
# Input: stones = [1]
# Output: 1
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        idx = len(stones) - 1
        while len(stones) > 1:
            stones = sorted(stones)
            if idx >= 1:
                if stones[idx] == stones[idx - 1]:
                    del stones[idx]
                    del stones[idx - 1]
                    idx -= 2
                else:
                    stones[idx] -= stones[idx - 1]
                    del stones[idx - 1]
                    idx -= 1
        return stones[0] if stones else 0

    def lastStoneWeight2(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_idx, max_el, prev_idx, prev_max = None, float('-inf'), None, float('-inf')
            for idx, stone in enumerate(stones):
                if stone > max_el:
                    prev_idx, max_idx = max_idx, idx
                    prev_max, max_el = max_el, stone
                if prev_max < stone and idx != max_idx:
                    prev_max, prev_idx = stone, idx
            if max_el == prev_max:
                if max_idx > prev_idx:
                    del stones[max_idx]
                    del stones[prev_idx]
                else:
                    del stones[prev_idx]
                    del stones[max_idx]
            else:
                stones[max_idx] -= prev_max
                del stones[prev_idx]
        return stones[0] if stones else 0

    def lastStoneWeight3(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while stones:
            stone_1 = stones.pop()
            if not stones:
                return stone_1
            stone_2 = stones.pop()
            if stone_1 > stone_2:
                for i in range(len(stones) + 1):
                    if i == len(stones) or stones[i] >= stone_1 - stone_2:
                        stones.insert(i, stone_1 - stone_2)
                        break
        return 0


if __name__ == '__main__':
    a = Solution()
    print(a.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(a.lastStoneWeight([1]))
    print(a.lastStoneWeight([2, 2]))
