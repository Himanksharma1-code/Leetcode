class Solution(object):
    def countSmaller(self, nums):
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(nums)))}
        bit = [0] * (len(ranks) + 1)

        def update(idx, delta):
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & (-idx)

        def query(idx):
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total

        res = []
        for x in reversed(nums):
            r = ranks[x]
            res.append(query(r - 1))
            update(r, 1)

        return res[::-1]