class Solution(object):
    def countDigitOne(self, n):
        count = 0
        factor = 1

        while factor <= n:
            divider = factor * 10
            count += (n // divider) * factor + min(max(n % divider - factor + 1, 0), factor)
            factor *= 10

        return count