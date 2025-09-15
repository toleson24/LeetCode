from typing import Dict, List, Set, Tuple
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: Dict[int, Set[str]] = defaultdict(set)
        cols: Dict[int, Set[str]] = defaultdict(set)
        boxes: Dict[Tuple[int, int], Set[str]] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or \
                   board[r][c] in cols[c] or \
                   board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[r].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
    
