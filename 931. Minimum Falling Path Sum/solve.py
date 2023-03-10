class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n-2,-1,-1):
            for j in range(0,n):
                n1 = matrix[i+1][j]
                n2 = float('inf')
                if j-1 >= 0:  n2 = matrix[i+1][j-1]
                n3 = float('inf')
                if j+1 < n:   n3 = matrix[i+1][j+1]
                matrix[i][j] += min(n1,n2,n3)
        res = float('inf')
        for num in matrix[0]:
            res = min(num,res)
        return res
        