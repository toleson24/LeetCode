from typing import List, Set, Tuple

# runtime: 44.78%, memory: 11.44%
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        _max_area: int = 0

        rows: int = len(grid)
        cols: int = len(grid[0])
        directions: Tuple[Tuple[int, int]] = ((1, 0), (-1, 0), (0, -1), (0, 1))

        visited: Set[Tuple[int, int]] = set()

        def dfs_iter(x: int, y: int) -> int:
            visited.add((x, y))
            stack: List[Tuple[int, int]] = [(x, y)]
            area = 1
            
            while stack:
                xc, yc = stack.pop()

                for dx, dy in directions:
                    nx, ny = xc + dx, yc + dy
                    if (
                        0 <= nx < rows and 0 <= ny < cols and 
                        grid[nx][ny] == 1 and (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        area += 1

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    _max_area = max(_max_area, dfs_iter(i, j))

        return _max_area

        