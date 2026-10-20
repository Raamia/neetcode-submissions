class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r < 0 or c < 0 or c >= len(grid[0]) or r>=len(grid) or grid[r][c] == "0":
                return False
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j):
                    count+=1
        return count