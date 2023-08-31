class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        dp = [0] + [float("INF") for i in range(n)]

        for i, tape in enumerate(ranges):
            begin, end = max(0, i-tape), min(n, i+tape)
            
            for j in range(begin, end):
                dp[end] = min(dp[end], dp[j]+1)

        return dp[n] if dp[n] != float("INF") else -1
