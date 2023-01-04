class Solution(object):
    def searchMatrix(self, m, t):
        a,b = len(m), len(m[0])
        i,j = 0,b-1
        while i < a and j >= 0 : 
            if m[i][j] < t : i+=1
            elif m[i][j] > t : j-=1
            else : return True
        return False  