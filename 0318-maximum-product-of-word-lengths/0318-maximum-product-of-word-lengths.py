class Solution(object):
    def maxProduct(self, words):
        masks = {}
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[mask] = max(masks.get(mask, 0), len(w))

        max_prod = 0
        for m1, len1 in masks.items():
            for m2, len2 in masks.items():
                if not (m1 & m2):
                    prod = len1 * len2
                    if prod > max_prod:
                        max_prod = prod

        return max_prod