class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.paths = 0 
        n, m  = len(grid), len(grid[0])
        obs, seen  = [], []
        def parc(i,j,s):
            global paths
            if i == end_x and j == end_y : 
                if s == result :
                    self.paths+=1
                return 
            if not (i < 0 or j < 0 or i > n-1 or j > m-1 ) and (i,j) not in seen and (i,j) not in obs: 
                seen.append((i,j))
                parc(i+1,j,s+1) or parc(i,j+1,s+1) or parc(i,j-1,s+1) or parc(i-1,j,s+1) 
                seen.pop()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    start_x, start_y = i, j 
                elif grid[i][j] == 2 :
                    end_x, end_y = i, j
                elif grid[i][j] == -1 :  
                    obs.append((i,j))
        result = n*m-1-len(obs)
        parc(start_x,start_y,0)
        return self.paths