import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        # Sort width ascending; for identical widths, sort height descending
        # to prevent choosing two envelopes with the same width.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Find the length of the Longest Increasing Subsequence (LIS) on heights
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)