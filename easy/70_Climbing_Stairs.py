# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:
        '''
        Space complexity O(n)
        Time complexity O(n)
        :param n:
        :return:
        '''
        lst = [0, 1, 2, 3]
        if n < 4:
            return lst[n]
        for i in range(3, n + 1):
            lst.append(lst[i] + lst[i - 1])
        return lst[n]

    def climbStairs3(self, n: int) -> int:
        '''
        Space complexity O(1)
        Time complexity O(n)
        :param n:
        :return:
        '''
        one, two = 1, 1
        for i in range(n):
            temp = one
            one += two
            two = temp
        return two


if __name__ == '__main__':
    a = Solution()
    print(a.climbStairs(44))
