class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    idx = int(board[r][c]) - 1
                    mask = 1 << idx
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def backtrack(cell_idx):
            if cell_idx == len(empty_cells):
                return True

            r, c = empty_cells[cell_idx]
            b = (r // 3) * 3 + (c // 3)

            
            avail = ~(rows[r] | cols[c] | boxes[b]) & 0x1FF

            while avail:
                
                lsb = avail & -avail
                avail ^= lsb 

                idx = lsb.bit_length() - 1
                rows[r] |= lsb
                cols[c] |= lsb
                boxes[b] |= lsb
                board[r][c] = str(idx + 1)

                if backtrack(cell_idx + 1):
                    return True

                rows[r] ^= lsb
                cols[c] ^= lsb
                boxes[b] ^= lsb
                board[r][c] = '.'

            return False

        backtrack(0)