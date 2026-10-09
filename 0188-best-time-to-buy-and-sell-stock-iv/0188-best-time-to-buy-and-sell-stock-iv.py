class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        n = len(prices)

        if k >= n // 2:
            return sum(
                max(0, prices[i] - prices[i - 1]) for i in range(1, n)
            )

        buy = [-float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]