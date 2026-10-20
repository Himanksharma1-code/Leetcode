class Solution(object):
    def maxProfit(self, prices):
        held = -float('inf')
        sold = 0
        rest = 0

        for price in prices:
            prev_sold = sold
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, prev_sold)

        return max(sold, rest)