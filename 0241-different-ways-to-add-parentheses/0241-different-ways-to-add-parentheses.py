class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def ways(expr):
            if expr in memo:
                return memo[expr]

            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = ways(expr[:i])
                    right = ways(expr[i + 1:])
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)

            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return ways(expression)