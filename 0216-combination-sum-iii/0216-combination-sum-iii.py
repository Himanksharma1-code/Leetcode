class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def backtrack(start, comb, target):
            if len(comb) == k:
                if target == 0:
                    res.append(list(comb))
                return

            for num in range(start, 10):
                if num > target:
                    break
                comb.append(num)
                backtrack(num + 1, comb, target - num)
                comb.pop()

        backtrack(1, [], n)
        return res