# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
#
# Input: jewels = "z", stones = "ZZ"
# Output: 0

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {el: 0 for el in jewels}
        for el in stones:
            if el in hashmap:
                hashmap[el] += 1
        return sum(hashmap.values())

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        st = set(jewels)
        return sum(1 for i in stones if i in st)
