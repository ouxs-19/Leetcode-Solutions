class Solution:
    def maximumRows(self, mat: List[List[int]], k: int) -> int:
        self.mx = 0 
        self.cols = []
        n,m = len(mat), len(mat[0])
        
        def count():
            cnt = 0 
            for row in mat :
                for i, val in enumerate(row):
                    if not (val==0 or i in self.cols) :break
                else : 
                    cnt+=1
            return cnt
        
        def solve(i, col):
            if i == k : 
                self.mx = max(self.mx,count())
                return 
            if col>m-k+i:
                return 
            self.cols.append(col)
            solve(i+1,col+1)
            self.cols.pop()
            solve(i,col+1)
        solve(0,0)
        return self.mx