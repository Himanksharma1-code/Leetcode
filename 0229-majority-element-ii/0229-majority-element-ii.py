class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []

        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        n = len(nums)
        for cand in set([cand1, cand2]):
            if cand is not None and nums.count(cand) > n // 3:
                res.append(cand)

        return res