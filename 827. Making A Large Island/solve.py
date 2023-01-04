class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        m = n 
        land = Counter()
        count,ans = 2,0
        cousins = [[1,0],[-1,0],[0,-1],[0,1]]
        def dfs(t,i,j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1: return
            land[t] += 1
            grid[i][j] = t
            for x, y in cousins: dfs(t, x+i, y+j)
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 1:
                dfs(count, x, y)
                count += 1
        for x, y in product(range(m), range(n)):
            if grid[x][y] != 0: continue
            neibs = set()
            for dx, dy in cousins:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x+dx][y+dy] != 0:
                    neibs.add(grid[x+dx][y+dy])
            ans = max(ans, sum(land[i] for i in neibs) + 1)
        return ans if ans != 0 else m*n