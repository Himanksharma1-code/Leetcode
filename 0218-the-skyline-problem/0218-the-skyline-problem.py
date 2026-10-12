import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        res = [[-1, 0]]
        live = [(0, float('inf'))]

        for x, neg_h, r in events:
            if neg_h != 0:
                heapq.heappush(live, (neg_h, r))
            while live[0][1] <= x:
                heapq.heappop(live)

            curr_h = -live[0][0]
            if res[-1][1] != curr_h:
                if res[-1][0] == x:
                    res[-1][1] = curr_h
                else:
                    res.append([x, curr_h])

        return res[1:]