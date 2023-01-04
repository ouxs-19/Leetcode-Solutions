from functools import lru_cache

class Solution:
    def minCut(self, s: str) -> int:
        x = lambda string : string == string[::-1]
        
        @lru_cache(maxsize=None)
        def solve(s) :
            n = len(s)
            if n == 0 : return 0
            count = float("inf")
            for i in range(1,n+1):
                if x(s[:i]) :
                    res = solve(s[i:])+1
                    if res < count  :
                        count = res
            return count
        if len(set(s)) ==1  : return 0
        result = solve(s)-1
        if result > 0 : return result
        return 0 
    
        