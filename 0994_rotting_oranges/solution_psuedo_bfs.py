from typing import List, Set, Tuple 

# runtime: 24.39, memory: 17.54%
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        directions: Tuple[Tuple[int, int]] = ((1, 0), (-1, 0), (0, -1), (0, 1))

        minutes: int = 0
        fresh: Set[Tuple[int, int]] = set()
        rotten: List[Tuple[int, int]] = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while fresh:
            if not rotten:
                return -1

            new_rotten: List[Tuple[int, int]] = []
            for i, j in rotten:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) in fresh:
                        fresh.remove((ni, nj))
                        new_rotten.append((ni, nj))

            if not new_rotten: 
                return -1
            
            rotten += new_rotten
            minutes += 1

        return minutes if not fresh else -1

        