from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,buy):
            if i >= len(prices) : return 0
            ans = dp(i+1, buy)
            if buy: ans = max(ans, dp(i+1, False) - prices[i])
            else: ans = max(ans, dp(i+2, True) + prices[i]) 
            return ans
        return dp(0, True)   