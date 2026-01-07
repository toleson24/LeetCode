from collections import deque 
from typing import Deque, List, Set, Tuple 

#runtime: 88.27%, memory: 17.54% 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        directions: Tuple[Tuple[int, int]] = ((1, 0), (-1, 0), (0, -1), (0, 1))

        minutes: int = 0
        fresh: Set[Tuple[int, int]] = set()
        rotten: Deque[Tuple[int, int]] = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while fresh and rotten: 
            level_size: int = len(rotten)
            for _ in range(level_size):
                i, j = rotten.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) in fresh:
                        fresh.remove((ni, nj))
                        rotten.append((ni, nj))
            
            minutes += 1

        return minutes if not fresh else -1

        