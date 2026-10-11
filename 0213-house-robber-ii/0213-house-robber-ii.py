class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for money in houses:
                rob1, rob2 = rob2, max(rob2, rob1 + money)
            return rob2

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))