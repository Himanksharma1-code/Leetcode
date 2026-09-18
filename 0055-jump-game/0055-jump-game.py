class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        target = len(nums) - 1

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            if i + jump > max_reach:
                max_reach = i + jump
            if max_reach >= target:
                return True

        return True