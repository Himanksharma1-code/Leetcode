class Solution(object):
    def addOperators(self, num, target):
        res = []
        n = len(num)

        def backtrack(index, prev_operand, current_val, expr):
            if index == n:
                if current_val == target:
                    res.append("".join(expr))
                return

            for i in range(index, n):
                if i > index and num[index] == '0':
                    break

                part = num[index:i + 1]
                val = int(part)

                if index == 0:
                    expr.append(part)
                    backtrack(i + 1, val, val, expr)
                    expr.pop()
                else:
                    expr.append('+')
                    expr.append(part)
                    backtrack(i + 1, val, current_val + val, expr)
                    expr.pop()
                    expr.pop()

                    expr.append('-')
                    expr.append(part)
                    backtrack(i + 1, -val, current_val - val, expr)
                    expr.pop()
                    expr.pop()

                    expr.append('*')
                    expr.append(part)
                    backtrack(i + 1, prev_operand * val, current_val - prev_operand + prev_operand * val, expr)
                    expr.pop()
                    expr.pop()

        backtrack(0, 0, 0, [])
        return res