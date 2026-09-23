class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(grid, r, c):
            if  r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1+dfs(grid, r+1,c)+ dfs(grid, r-1, c)+ dfs(grid, r, c+1)+ dfs(grid, r, c-1)
        sol = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sol = max(sol,dfs(grid, i, j))
        return sol