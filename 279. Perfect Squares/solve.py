class Solution:
    def numSquares(self, amount: int) -> int:
        coins = []
        if amount == 1 : return 1 
        for i in range(1,amount):
            s = i*i
            if s > amount :
                break
            coins.append(s)
            
        dp = [0]+ [-1]*(amount)
        for coin in coins:
            for x in range(amount+1):
                if dp[x] !=-1 and x+coin <= amount:
                    if dp[x+coin] == -1: dp[x+coin] = dp[x]+1
                    else: dp[x+coin]= min(dp[x+coin],dp[x]+1)
        return dp[-1]