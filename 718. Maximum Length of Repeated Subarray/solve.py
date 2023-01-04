class Solution:
    def findLength(self, X: List[int], Y: List[int]) -> int:
        l1, l2 = len(X), len(Y)
        dp = [ [0 for _ in range(l2+1)] for i in range(l1+1)]
        
        for i in range(l1):
            for j in range(l2):
                if X[i] == Y[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        return max(max(row) for row in dp)