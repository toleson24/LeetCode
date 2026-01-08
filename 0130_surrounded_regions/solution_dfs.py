from typing import List 

# runtime: 86.07%, memory: 17.99% 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: int = len(board)
        cols: int = len(board[0])
        
        def dfs(x: int, y: int) -> None:
            board[x][y] = '#'  # protected
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                    dfs(nx, ny)
        
        # dfs from 'O's on border
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)
        
        # flip surrounding regions 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # flip to 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'  # revert to 'O'

        return

        