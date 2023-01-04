class Solution:
    def maximumScore(self, nums: List[int], m: List[int]) -> int:
        l = len(m)
        dp = [0] * (l + 1)
        for i in range(l-1,-1,-1):
            tmp_dp = [0]*(i + 1)
            for j in range(i,-1,-1):
                tmp_dp[j] = max(dp[j + 1] + m[i] * nums[j], dp[j] + m[i] * nums[~(i-j)])
            dp = tmp_dp
        return dp[0]
