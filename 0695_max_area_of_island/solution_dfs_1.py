from collections import deque 
from typing import Deque, List, Set, Tuple 

# runtime: 8.71, memory: 8.85
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        _max_area: int = 0

        rows: int = len(grid)
        cols: int = len(grid[0])
        directions: Tuple[Tuple[int, int]] = ((1, 0), (-1, 0), (0, -1), (0, 1))

        islands: Deque[Tuple[int, int]] = deque((i, j) for i in range(rows) for j in range (cols) if grid[i][j] == 1)

        visited: Set[Tuple[int, int]] = set()

        # def dfs(x: int, y: int, area: int) -> int:
        #     # visited: Set[Tuple[int, int]] = set()
        #     visited.add((x, y))
            
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:
        #             return dfs(nx, ny, area + 1)

        #     return area

        def dfs_iter(x: int, y: int, area: int) -> int:
            visited.add((x, y))
            stack: List[Tuple[int, int]] = []
            stack.append((x, y))
            
            while stack:
                xc, yc = stack.pop()

                for dx, dy in directions:
                    nx, ny = xc + dx, yc + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        area += 1

            return area

        for x, y in islands:
            # _max_area = max(_max_area, dfs(x, y, 1))
            _max_area = max(_max_area, dfs_iter(x, y, 1))

        return _max_area

        