class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1 for i in range(maxMove+1)] for j in range(m)] for k in range(n)]
        
        def solve(i,j,left):
            if i < 0 or j < 0 or i == n or j == m : return 1
            if left == 0 : return 0
            if dp[i][j][left] >= 0 : return dp[i][j][left]
            dp[i][j][left] = solve(i-1,j,left-1)+solve(i,j-1,left-1)+solve(i+1,j,left-1)+solve(i,j+1,left-1)
            return dp[i][j][left]
        return solve(startRow,startColumn,maxMove) %1000000007