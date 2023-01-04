from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def count(i):
            if i == n : return 1 
            if s[i]== '0' : return 0
            if i == n-1 : return 1 
            if '09'<s[i:i+2] <'27':
                return count(i+2)+count(i+1)
            else :
                return count(i+1)
        return count(0)