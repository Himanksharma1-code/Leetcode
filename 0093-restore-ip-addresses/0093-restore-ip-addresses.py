class Solution:
    def restoreIpAddresses(self, s):
        res = []

        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start : start + length]

                if (segment.startswith("0") and len(segment) > 1) or int(
                    segment
                ) > 255:
                    continue

                backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return res