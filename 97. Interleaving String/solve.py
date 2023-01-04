class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        li, lj, lk = len(s1), len(s2), len(s3)
        
        @cache
        def solve(i,j,k):
            if k == lk :
                if i == li and j == lj : 
                    return True
                else : 
                    return False 
            elif i == li : 
                if s2[j] == s3[k] :
                    return solve(i,j+1,k+1) 
            elif j == lj : 
                if s1[i] == s3[k] : 
                    return solve(i+1,j,k+1) 
            elif s1[i] == s3[k] and s2[j] == s3[k] : 
                return solve(i+1,j,k+1) or solve(i,j+1,k+1) 
            elif  s2[j] == s3[k] : 
                return  solve(i,j+1,k+1) 
            elif s1[i] == s3[k]  : 
                return solve(i+1,j,k+1)
            return False 
        if lk != li + lj : return False 
        return solve(0,0,0)