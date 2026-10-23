class Solution(object):
    def minPatches(self, nums, n):
        miss = 1
        patches = 0
        i = 0
        length = len(nums)

        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches