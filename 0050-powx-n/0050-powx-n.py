class Solution(object):
    def myPow(self, x, n):
        exp = n
        if exp < 0:
            x = 1.0 / x
            exp = -exp

        result = 1.0
        while exp > 0:
            if exp % 2 == 1:
                result *= x
            x *= x
            exp //= 2

        return result