class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        below_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [below_twenty[n]]
            elif n < 100:
                return [tens[n // 10]] + helper(n % 10)
            else:
                return [below_twenty[n // 100], "Hundred"] + helper(n % 100)

        res = []
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                chunk = helper(num % 1000)
                if unit:
                    chunk.append(unit)
                res = chunk + res
            num //= 1000

        return " ".join(res)