class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0

        for r in range(rows):
            for c in range(cols):
                temp = dp[c + 1]
                if matrix[r][c] == "1":
                    dp[c + 1] = min(dp[c], dp[c + 1], prev) + 1
                    if dp[c + 1] > max_side:
                        max_side = dp[c + 1]
                else:
                    dp[c + 1] = 0
                prev = temp

        return max_side * max_side