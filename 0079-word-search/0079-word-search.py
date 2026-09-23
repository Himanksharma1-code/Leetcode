from collections import Counter


class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False

        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)

        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def backtrack(r, c, idx):
            if idx == len(word):
                return True

            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or board[r][c] != word[idx]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, idx + 1)
                or backtrack(r - 1, c, idx + 1)
                or backtrack(r, c + 1, idx + 1)
                or backtrack(r, c - 1, idx + 1)
            )

            board[r][c] = temp
            return found

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False