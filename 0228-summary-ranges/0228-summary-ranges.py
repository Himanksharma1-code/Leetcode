class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(nums[i]))
            i += 1

        return ranges