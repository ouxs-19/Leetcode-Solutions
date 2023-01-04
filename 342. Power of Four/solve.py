from math import log 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 : 
            res = log(n,4)
            return res == int(res)
        return False 