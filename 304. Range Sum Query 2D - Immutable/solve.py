class NumMatrix(object):

    def __init__(self, matrix):
        M, N = len(matrix), len(matrix[0])
        self.prefix_sum = [[0 for _ in range(N)] for _ in range(M)]
        self.prefix_sum[0][0] =  matrix[0][0]
        for i in range(1, M):
            self.prefix_sum[i][0] = matrix[i][0] + self.prefix_sum[i-1][0]
        for j in range(1, N):
            self.prefix_sum[0][j] = matrix[0][j] + self.prefix_sum[0][j-1]
        for i in range(1, M):
            for j in range(1, N):
                self.prefix_sum[i][j] = matrix[i][j]+self.prefix_sum[i-1][j]+self.prefix_sum[i][j-1]-self.prefix_sum[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        if row1 > 0 and col1 > 0:
            return self.prefix_sum[row2][col2]-self.prefix_sum[row1-1][col2]-self.prefix_sum[row2][col1-1]+self.prefix_sum[row1-1][col1-1]
        elif row1 > 0:
            return self.prefix_sum[row2][col2]-self.prefix_sum[row1-1][col2]
        elif col1 > 0:
            return self.prefix_sum[row2][col2]-self.prefix_sum[row2][col1-1]
        else:
            return self.prefix_sum[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)