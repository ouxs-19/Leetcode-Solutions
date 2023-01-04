mod = 10**9+7
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        workers = []
        res,s = 0,0 
        for i, j in sorted(zip(efficiency, speed),reverse=True):
            while len(workers) > k-1:
                s -= heappop(workers)
            heappush(workers, j)
            s += j
            res = max(res, s * i)
            
        return res % mod