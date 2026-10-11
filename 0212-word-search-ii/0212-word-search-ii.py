class Solution(object):
    def findWords(self, board, words):
     
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word  

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node[char]

            if '#' in curr_node:
                res.append(curr_node['#'])
                del curr_node['#']

            board[r][c] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in curr_node:
                        dfs(nr, nc, curr_node)

            board[r][c] = char

            if not curr_node:
                parent_node.pop(char)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res