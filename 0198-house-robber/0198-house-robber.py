class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + num)
        return rob2