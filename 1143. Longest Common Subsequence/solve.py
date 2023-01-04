from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        @lru_cache(None)
        def lcs(m, n):
            if m == 0 or n == 0:
                return 0
            elif X[m-1] == Y[n-1]:
                return 1 + lcs(m-1, n-1)
            else:
                return max(lcs(m, n-1), lcs(m-1, n))
        return lcs(len(X),len(Y))