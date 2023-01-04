class Solution(object):
    def longestPalindromeSubseq(self, s):
        dp = [1] * len(s)
        pre = None
        for j in range(1, len(s)):
            for i in range(j - 1, -1, -1):
                temp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + (pre if j > i + 1 else 0)
                else:
                    dp[i] = max(dp[i], dp[i + 1])
                pre = temp
                    
        return dp[0]