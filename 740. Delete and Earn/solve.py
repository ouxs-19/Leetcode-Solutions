import collections
from functools import *
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vector = [0]*(max(nums)+1)
        for i in range(len(nums)):
            vector[nums[i]]+=1
        dp = [0]*(max(nums)+1)
        dp[0] = 0 
        dp[1] = vector[1]
        for i in range(2,max(nums)+1):
            dp[i] = max(dp[i-1],dp[i-2]+vector[i]*i)
        return dp[max(nums)]