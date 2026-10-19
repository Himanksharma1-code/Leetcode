class Solution(object):
    def numSquares(self, n):
        def is_square(x):
            s = int(x**0.5)
            return s * s == x

        if is_square(n):
            return 1

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        for i in range(1, int(n**0.5) + 1):
            if is_square(n - i * i):
                return 2

        return 3