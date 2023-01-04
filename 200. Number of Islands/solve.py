class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l0, l1 = len(grid), len(grid[0])
        number = 0 
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        for i in range(l0):
            for j in range(l1):
                if grid[i][j] == "1":
                    dfs(grid,i,j)
                    number+=1
        return number
