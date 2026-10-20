class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        days = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        while fresh > 0 and queue:
            lenq = len(queue)
            for i in range(lenq):
                curr = queue.popleft()
                r = curr[0]
                c = curr[1]
                if r+1 < len(grid) and grid[r+1][c] == 1:
                    fresh-=1
                    grid[r+1][c] = 2
                    queue.append((r+1,c))
                if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                    fresh-=1
                    grid[r][c+1] = 2
                    queue.append((r,c+1))
                if r > 0 and grid[r-1][c] == 1:
                    fresh-=1
                    grid[r-1][c] = 2
                    queue.append((r-1,c))
                if c >0 and grid[r][c-1] == 1:
                    fresh-=1
                    grid[r][c-1] = 2
                    queue.append((r,c-1))
            days+=1
        if fresh == 0:
            return days
        else:
            return -1