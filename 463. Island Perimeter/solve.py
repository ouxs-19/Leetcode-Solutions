class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m  = len(grid) , len(grid[0]) 
        s =  0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 : 
                    cnt = 0
                    if i >0 and grid[i-1][j] == 1  :
                        cnt+=1
                    if j > 0 and grid [i][j-1]: 
                        cnt+=1                    
                    if i < n-1 and grid [i+1][j]: 
                        cnt+=1                        
                    if j <m-1 and grid [i][j+1]: 
                        cnt+=1
                    s+=4-cnt
        return s 