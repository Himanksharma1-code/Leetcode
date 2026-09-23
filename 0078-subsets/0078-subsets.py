class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, current):
            res.append(list(current))
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return res