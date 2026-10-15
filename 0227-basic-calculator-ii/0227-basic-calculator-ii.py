class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if char not in "+-*/" and not char.isdigit():
                    pass
                else:
                    pass
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)
                sign = char
                num = 0

        return sum(stack)