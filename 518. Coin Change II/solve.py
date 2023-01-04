from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+ [0]*(amount)
        for coin in coins:
            for x in range(amount+1):
                if x+coin <= amount:
                    dp[x+coin]+=dp[x]
        return dp[-1]