import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = [0] * n
        ugly[0] = 1

        pq = [(p, p, 0) for p in primes]
        heapq.heapify(pq)

        for i in range(1, n):
            ugly[i] = pq[0][0]
            while pq and pq[0][0] == ugly[i]:
                _, p, idx = heapq.heappop(pq)
                heapq.heappush(pq, (p * ugly[idx + 1], p, idx + 1))

        return ugly[-1]