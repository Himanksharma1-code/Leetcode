from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return []

        parents = defaultdict(list)
        layer = {beginWord}
        found = False

        while layer and not found:
            words -= layer
            next_layer = set()

            for word in layer:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + c + word[i + 1 :]
                        if next_word in words:
                            if next_word == endWord:
                                found = True
                            next_layer.add(next_word)
                            parents[next_word].append(word)

            layer = next_layer

        if not found:
            return []

        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return

            for parent in parents[word]:
                backtrack(parent, path + [parent])

        backtrack(endWord, [endWord])
        return res