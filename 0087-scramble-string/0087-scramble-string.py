class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dfs(s1, s2):
            key = (s1, s2)
            if key in memo:
                return memo[key]

            if s1 == s2:
                memo[key] = True
                return True

            if sorted(s1) != sorted(s2):
                memo[key] = False
                return False

            n = len(s1)
            for i in range(1, n):
                if (dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) or (
                    dfs(s1[:i], s2[n - i :]) and dfs(s1[i:], s2[: n - i])
                ):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(s1, s2)
        