class Solution:
    def minimumLines(self, stock_prices: list[list[int]]) -> int:
        length = len(stock_prices)
        if length == 1:
            return 0

        stock_prices.sort(key=lambda x: x[0])

        count = 1
        for i in range(2, length):
            Ax, Ay = stock_prices[i]
            Bx, By = stock_prices[i - 1]
            Cx, Cy = stock_prices[i - 2]
            if (Ay - By) * (Bx - Cx) != (Ax - Bx) * (By - Cy):
                count += 1

        return count

