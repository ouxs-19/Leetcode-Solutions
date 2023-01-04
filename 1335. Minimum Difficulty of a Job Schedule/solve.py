class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        nb_jobs = len(jobDifficulty)
        
        @cache
        def dp(i,j,k):
            if i == nb_jobs and j == 0: return k
            if i >= nb_jobs or  j <= 0: return inf
            return min(dp(i+1,j,max(k,jobDifficulty[i])),
                       max(k,jobDifficulty[i])+dp(i+1,j-1,0))
       
        ans = dp(0,d,0)
        return ans if ans != inf else -1