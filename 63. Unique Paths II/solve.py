class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if  grid[0][0]  : return 0
        grid[0][0] = 1 
        for i in range(1,m):
            if grid[0][i] == 1 : grid[0][i] = 0 
            else : grid[0][i] = 1 and grid[0][i-1]
        for i in range(1,n):
            if grid[i][0] == 1 : grid[i][0] = 0 
            else : grid[i][0] = 1 and grid[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1 : grid[i][j] = 0 
                else : grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]