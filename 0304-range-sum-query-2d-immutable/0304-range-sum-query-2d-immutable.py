class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.dp[r][c + 1]
                    + self.dp[r + 1][c]
                    - self.dp[r][c]
                )

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )