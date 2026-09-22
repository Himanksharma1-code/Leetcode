class Solution:
    def combine(self, n, k):
        res = []

        def backtrack(start, current):
            if len(current) == k:
                res.append(list(current))
                return

            # Prune search space when remaining numbers are insufficient
            for num in range(start, n - (k - len(current)) + 2):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])
        return res