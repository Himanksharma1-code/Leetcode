from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for val, count in (c1 & c2).items():
            res.extend([val] * count)
        return res