class Solution(object):
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1
        res = []

        for i in range(n - 1, 0, -1):
            idx = k // fact
            res.append(str(numbers.pop(idx)))
            k %= fact
            fact //= i

        res.append(str(numbers[0]))
        return "".join(res)