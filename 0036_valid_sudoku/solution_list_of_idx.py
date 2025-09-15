from typing import List, Tuple

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        idx_list: List[Tuple] = []

        for r, row in enumerate(board):
            for c, num in enumerate(row):
                if num != ".":
                    idx_list += [(r, num), (num, c), (r // 3, c // 3, num)]
        
        return len(idx_list) == len(set(idx_list))
    
    