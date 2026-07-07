class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0

        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10

            
            if rev > (INT_MAX - pop) // 10:
                return 0

            rev = rev * 10 + pop

        return sign * rev
        