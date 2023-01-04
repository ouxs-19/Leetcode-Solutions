class Solution:
    def combinationSum4(self, nums: List[int], amount: int) -> int:
        dp = [1]+[0]*amount
        for i in range(1,amount+1):
            for num in nums :
                if (s:=i-num) >= 0 :
                    dp[i] += dp[s]
        return dp[amount]  