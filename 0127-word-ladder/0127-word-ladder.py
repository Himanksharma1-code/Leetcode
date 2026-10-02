class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        length = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            word_set -= begin_set

            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + c + word[i + 1 :]
                        if next_word in end_set:
                            return length + 1
                        if next_word in word_set:
                            next_set.add(next_word)

            begin_set = next_set
            length += 1

        return 0