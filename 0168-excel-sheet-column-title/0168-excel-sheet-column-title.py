class Solution:
    def convertToTitle(self, columnNumber):
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            res.append(chr(ord('A') + (columnNumber % 26)))
            columnNumber //= 26
        return "".join(reversed(res))