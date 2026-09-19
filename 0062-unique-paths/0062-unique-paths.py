class Solution(object):
    def uniquePaths(self, m, n):
        total_steps = m + n - 2
        k = min(m - 1, n - 1)
        res = 1

        for i in range(1, k + 1):
            res = res * (total_steps - k + i) // i

        return res