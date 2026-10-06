class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                min_health_needed = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = max(1, min_health_needed)

        return dp[0][0]