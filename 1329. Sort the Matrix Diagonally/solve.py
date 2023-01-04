class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        total_num = n * m

        for i in range(1, n + m - 2):
            if i < n:start_row, start_col = n - i - 1, 0
            else:start_row, start_col = 0, i - n + 1
            diag = []
            while start_row < n and start_col < m:
                diag.append(mat[start_row][start_col])
                start_row += 1
                start_col += 1

            diag.sort()
            start_row -= 1
            start_col -= 1
            while start_row >= 0 and start_col >= 0:
                mat[start_row][start_col] = diag.pop()
                start_row -= 1
                start_col -= 1

        return(mat)