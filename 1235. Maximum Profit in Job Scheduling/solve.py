from functools import lru_cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        @lru_cache(None)
        def dp(i):
            if i == n: return 0
            ans = dp(i + 1)  
            for j in range(i + 1, n + 1):
                if j == n or jobs[j][0] >= jobs[i][1]:
                    ans = max(ans, dp(j) + jobs[i][2]) 
                    break
            return ans
        
        jobs = sorted(list(zip(startTime, endTime, profit)))
        return dp(0)