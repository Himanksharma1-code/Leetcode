class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            val = matrix[r][c]
            res = 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > val:
                    res = max(res, 1 + dfs(nr, nc))

            memo[(r, c)] = res
            return res

        return max(dfs(r, c) for r in range(m) for c in range(n))