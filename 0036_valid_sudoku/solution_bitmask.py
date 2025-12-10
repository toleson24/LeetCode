from typing import List 

# runtime: 81.48%, memory: 24.54% 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[int] = [0] * 9
        cols: List[int] = [0] * 9
        blox: List[int] = [0] * 9

        for i in range(9):
            for j in range(9):
                ch: str = board[i][j]
                if ch == ".":
                    continue
                x: int = (ord(ch) - ord('0')) % 9

                if (rows[i] >> x) & 1: 
                    return False
                rows[i] |= 1 << x

                if (cols[j] >> x) & 1:
                    return False
                cols[j] |= 1 << x

                idx: int = i // 3 * 3 + j // 3
                if (blox[idx] >> x) & 1:
                    return False
                blox[idx] |= 1 << x

        return True

        