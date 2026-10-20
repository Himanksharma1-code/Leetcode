class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            n1 = int(num[:i])

            for j in range(i + 1, n):
                if num[i] == '0' and j > i + 1:
                    break
                n2 = int(num[i:j])

                first, second = n1, n2
                k = j
                while k < n:
                    nxt = first + second
                    nxt_str = str(nxt)
                    if not num.startswith(nxt_str, k):
                        break
                    k += len(nxt_str)
                    first, second = second, nxt

                if k == n:
                    return True

        return False