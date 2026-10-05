from collections import defaultdict


class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_pts = 1

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slopes[(dx, dy)] += 1

            if slopes:
                max_pts = max(max_pts, max(slopes.values()) + 1)

        return max_pts