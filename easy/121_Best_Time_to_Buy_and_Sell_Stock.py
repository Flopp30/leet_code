# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        Space complexity O(1)
        Time complexity O(n)
        :param prices:
        :return:
        '''
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

    def maxProfit2(self, prices: list[int]) -> int:
        '''
        Space complexity O(1)
        Time complexity O(n)
        :param prices:
        :return:
        '''
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
        return profit
