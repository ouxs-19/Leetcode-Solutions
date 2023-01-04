class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxvalue ,best = (0,0)
        for i in range(len(values)):
            best = max(maxvalue+values[i]-i,best)
            maxvalue = max(maxvalue,values[i]+i)
        return best