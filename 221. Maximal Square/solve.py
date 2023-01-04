class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        prev, curr = [0]*(1+c), [0]*(1+c)
        maximum = 0
        for i in range(r):
            for j in range(1,1+c):
                if matrix[i][j-1]=="1":
                    curr[j]=1+min(curr[j-1],prev[j],prev[j-1])
            maximum = max(maximum,max(curr))
            prev = curr
            curr = [0]*(1+c)
        return maximum**2