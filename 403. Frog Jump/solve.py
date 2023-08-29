class Solution:
    def canCross(self, stones: List[int]) -> bool:

        @cache
        def dfs(x, y):
            if x == stones[-1] : return True
            return any(i and x+i in stones and dfs(x+i,i) for i in range(y-1,y+2))
        
        return dfs(0,0)