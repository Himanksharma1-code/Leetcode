class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        
        ans = 10
        unique_digits = 9
        available = 9
        
        for _ in range(2, n + 1):
            unique_digits *= available
            ans += unique_digits
            available -= 1
            
        return ans