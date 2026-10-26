from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        return [item for item, _ in Counter(nums).most_common(k)]