class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def max_single(nums, count):
            drop = len(nums) - count
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:count]

        def merge(a, b):
            res = []
            i = 0
            j = 0
            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res

        m, n = len(nums1), len(nums2)
        best = []

        start = max(0, k - n)
        end = min(k, m)

        for i in range(start, end + 1):
            candidate = merge(max_single(nums1, i), max_single(nums2, k - i))
            if candidate > best:
                best = candidate

        return best