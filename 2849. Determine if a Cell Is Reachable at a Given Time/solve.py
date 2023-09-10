class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1 : return False
        diag = abs(fy-sy)
        t -= diag 
        if t < 0  : return False
        diffX = abs(sx-fx)
        if diffX < 0 : 
            return True
        diffX -= diag 
        
        return diffX <= t
            