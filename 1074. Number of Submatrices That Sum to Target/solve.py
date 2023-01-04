class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], t: int) -> int:
        n =  len(matrix[0])
        res = 0
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j-1]
        for j in range(n):
            for k in range(j, n):
                mem, ssum = {0: 1}, 0
                for row in matrix:
                    ssum += row[k] - (row[j-1] if j else 0)
                    if ssum - t in mem: res += mem[ssum-t]
                    mem[ssum] = mem[ssum] + 1 if ssum in mem else 1  
        return res