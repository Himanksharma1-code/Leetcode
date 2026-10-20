from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        secret_counts = Counter()
        guess_counts = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] += 1
                guess_counts[g] += 1

        cows = sum(min(secret_counts[ch], guess_counts[ch]) for ch in guess_counts)

        return str(bulls) + "A" + str(cows) + "B"