class Solution(object):
    def palindromePairs(self, words):
        lookup = {word: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suff = word[j:]

                if pref == pref[::-1]:
                    rev_suff = suff[::-1]
                    if rev_suff in lookup and lookup[rev_suff] != i:
                        res.append([lookup[rev_suff], i])

                if j < n and suff == suff[::-1]:
                    rev_pref = pref[::-1]
                    if rev_pref in lookup and lookup[rev_pref] != i:
                        res.append([i, lookup[rev_pref]])

        return res