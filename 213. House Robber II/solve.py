class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        def solve(nums):
            n = len(nums)
            if n == 0 : return 0 
            if n == 1 : return nums[0]
            if n == 2 : return max(nums[1],nums[0])
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[2]+nums[0]
            i = 3 
            while i < n : 
                dp[i] = nums[i]+max(dp[i-2],dp[i-3])
                i+=1
            return max(dp[n-1],dp[n-2])
        if m == 1 : return nums[0]
        if m == 2 : return max(nums)
        return max(solve(nums[:-1]),solve(nums[1:]))