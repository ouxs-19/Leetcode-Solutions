class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        l = len(stations)
        dp = [startFuel]+[0]*l
        for i in range(l):
            for j in range(i,-1,-1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])
        for i in range(l+1):
            if dp[i] >= target : return i 
            
        return -1