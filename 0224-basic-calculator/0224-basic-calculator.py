class Solution(object):
    def calculate(self, s):
        stack = []
        operand = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                sign = 1
                operand = 0
            elif char == '-':
                result += sign * operand
                sign = -1
                operand = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                operand = 0

        return result + sign * operand