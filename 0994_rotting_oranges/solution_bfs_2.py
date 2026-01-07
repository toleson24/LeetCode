from collections import deque
from typing import Deque, List, Tuple 

#runtime: 81.24%, memory: 17.54%
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        fresh: int = 0
        rotten: Deque[Tuple[int, int]] = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        if fresh == 0:
            return 0
        
        directions: Tuple[Tuple[int, int]] = ((1, 0), (-1, 0), (0, -1), (0, 1))
        minutes: int = 0

        while rotten and fresh > 0: 
            n_rotten_this_min: int = len(rotten)
            for _ in range(n_rotten_this_min):
                i, j = rotten.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        rotten.append((ni, nj))
            
            minutes += 1

        return minutes if not fresh else -1

        