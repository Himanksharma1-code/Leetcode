import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        
        if m > n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m
            
        ans = -float('inf')
        
        for r1 in range(m):
            row_sums = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    row_sums[c] += matrix[r2][c]
                
                max_kadane = -float('inf')
                curr_kadane = 0
                for s in row_sums:
                    curr_kadane = max(s, curr_kadane + s)
                    if curr_kadane > max_kadane:
                        max_kadane = curr_kadane
                
                if max_kadane <= k:
                    ans = max(ans, max_kadane)
                    if ans == k:
                        return k
                    continue
                
                sorted_pref = [0]
                pref = 0
                for s in row_sums:
                    pref += s
                    idx = bisect.bisect_left(sorted_pref, pref - k)
                    if idx < len(sorted_pref):
                        ans = max(ans, pref - sorted_pref[idx])
                        if ans == k:
                            return k
                    bisect.insort(sorted_pref, pref)
                    
        return ans