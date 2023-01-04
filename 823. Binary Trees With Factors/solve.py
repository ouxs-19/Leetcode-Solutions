mod =  10 ** 9 + 7
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        dp = [1]*n
        for i, n in enumerate(arr):
            for j in range(i):
                if not n % arr[j] : 
                    r = n // arr[j]
                    if r in arr : 
                        dp[i]+=dp[j]*dp[arr.index(r)]
        return sum(dp) % mod