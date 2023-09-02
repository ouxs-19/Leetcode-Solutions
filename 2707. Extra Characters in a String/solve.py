class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n = len(s)

        @cache
        def dp(ind):
            if ind == n : 
                return 0
            
            left = dp(ind+1) + 1
            for i in range(ind+1, n+1):
                if s[ind:i] in dictionary : 
                    left = min(left, dp(i))
            
            return left
        
        return dp(0)