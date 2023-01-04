class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        lower = [float("inf")] * (k + 1)
        best = [0] * (k + 1)
        
        for p in prices:
            for i in range(1, k + 1):
                lower[i] = min(lower[i],p-best[i-1])
                best[i] = max(best[i], p - lower[i])
        return best[k]
