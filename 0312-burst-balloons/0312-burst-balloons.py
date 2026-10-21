class Solution(object):
    def maxCoins(self, nums):
        vals = [1] + [x for x in nums if x > 0] + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = vals[left] * vals[k] * vals[right] + dp[left][k] + dp[k][right]
                    if coins > dp[left][right]:
                        dp[left][right] = coins

        return dp[0][n - 1]