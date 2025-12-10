from typing import List, Set

# runtime: 5.61%, memory: 43.53% 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[Set[int]] = [set() for _ in range(9)]
        cols: List[Set[int]] = [set() for _ in range(9)]
        blox: List[Set[int]] = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ch: str = board[i][j]
                if ch == ".":
                    continue
                x: int = (ord(ch) - ord('0')) % 9

                if x in rows[i]:
                    return False
                rows[i].add(x)

                if x in cols[j]:
                    return False
                cols[j].add(x)

                idx: int = i // 3 * 3 + j // 3
                if x in blox[idx]:
                    return False
                blox[idx].add(x)

        return True

        