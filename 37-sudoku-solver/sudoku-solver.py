class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        row, col, cell = [0] * 9, [0] * 9, [0] * 9
        empty = set()
        for i, j in product(range(9), repeat = 2):
            k = i - i % 3 + j // 3
            if board[i][j] == '.':
                empty.add((i, j, k))
            else:
                mask = 1 << (ord(board[i][j]) - ord('1'))
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask

        def bt():
            if not empty:
                return True
            # Select an empty cell with the most digits used
            max_cnt_num = 0
            for ii, jj, kk in empty:
                # cnt_num - number of digits used
                cnt_num = (row[ii] | col[jj] | cell[kk]).bit_count()
                if cnt_num > max_cnt_num:
                    max_cnt_num = cnt_num
                    i, j, k = ii, jj, kk

            full_mask = 0b111111111 - (row[i] | col[j] | cell[k])
            empty.remove((i, j, k))
            while full_mask:
                n = full_mask.bit_length() - 1
                mask = 1 << n
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask
                if bt():
                    board[i][j] = chr(n + ord('1'))
                    return True
                row[i] ^= mask
                col[j] ^= mask
                cell[k] ^= mask
                full_mask ^= mask
            empty.add((i, j, k))
            return False
            
        bt()