class Solution:
    def numRollsToTarget(self, m: int, k: int, target: int) -> int:
        @cache
        def solve(s, t):
            if t == m: return 1 if s == target else 0
            combs = 0
            for i in range(1, min(k + 1, target - s + 1)):
                combs += solve(s+i,t+1)
            return combs
        return solve(0, 0) % 1000000007