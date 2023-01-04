class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        acc, n = [0] + list(accumulate(map(int, s))), len(s)
        return min(2*acc[i] + n - i - acc[-1] for i in range(n+1))