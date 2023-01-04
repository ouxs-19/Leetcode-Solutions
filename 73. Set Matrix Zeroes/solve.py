class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n , m = len(matrix) , len(matrix[0])
        r , c = set() , set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    r.add(i)
                    c.add(j)
        for i in range(n):
            for j in range(m):
                if i in r or j in c : matrix[i][j] = 0 
